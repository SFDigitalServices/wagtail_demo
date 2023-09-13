import pytest
import wagtail_factories
from cms import models
from playwright.sync_api import expect
from wagtail.models import Page, Site

import os

os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


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
def not_homepage(site_home):
    np = HomePageFactory.build(parent=site_home)
    site_home.add_child(instance=np)
    return np


@pytest.mark.django_db
def test_homepage(page, admin_user, not_homepage):
    resp = page.goto(not_homepage.full_url)
    assert resp.status == 200
    breakpoint()
    expect(page).to_have_title(not_homepage.title)
