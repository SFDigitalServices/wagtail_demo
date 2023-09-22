import pytest
import wagtail_factories
from cms import models
from playwright.sync_api import expect
from wagtail.models import Page, Site
from dataclasses import dataclass
import os

os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")

@dataclass

class RichTextFactory:

    source: str


class WidgetDocumentPageFactory(wagtail_factories.PageFactory):
    title = 'widget title'
    body = wagtail_factories.StreamFieldFactory({
        'paragraph': RichTextFactory(source="<p>test</p>"),
    })
    description = 'description'
    class Meta:
        model = models.WidgetDocumentation
class HomePageFactory(wagtail_factories.PageFactory):
    title = "test page"

    class Meta:
        model = models.HomePage


@pytest.fixture
def site_home(live_server):
    site = Site.objects.all().first()
    port = live_server.url.split(":")[-1]
    site.port = port
    site.save()
    home = Page.objects.get(slug="home")
    return home


@pytest.fixture
def wid_doc(site_home):
    np = WidgetDocumentPageFactory.build(
        parent=site_home,
        body__0='paragraph',
        body__1='paragraph',
    )
    site_home.add_child(instance=np)
    return np


@pytest.fixture
def not_homepage(site_home):
    np = HomePageFactory.build(parent=site_home)
    site_home.add_child(instance=np)
    return np


@pytest.mark.django_db
def test_homepagex(page, admin_user, wid_doc):

    resp = page.goto(wid_doc.full_url)
    assert resp.status == 200
    # expect(page).to_have_title(not_homepage.title)
    # number_of_ps = 2
    # soup = BS(resp.text())
    # assert(number_of_ps, len(soup.find('p.toc')))
    # tocs = soup.find('li.toc')
    # assert(number_of_ps, len(tocs))
    # assertEquals('first para', tocs[0].text)
    # assertEquals('second para', tocs[1].text)




@pytest.mark.django_db
def test_homepage(page, admin_user, not_homepage):
    resp = page.goto(not_homepage.full_url)
    assert resp.status == 200
    expect(page).to_have_title(not_homepage.title)

    print(resp.text)
    assert True==False