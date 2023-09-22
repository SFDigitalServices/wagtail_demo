from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks


class HomePage(Page):
    pass


class WidgetDocumentation(Page):

    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ], use_json_field=True)
    description = models.CharField(max_length=255)
    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('body'),
    ]

