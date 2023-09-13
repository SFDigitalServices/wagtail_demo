import os
from config.settings.base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "wagtail_demo.sqlite3",
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# TODO: figure out later
WAGTAILADMIN_BASE_URL = "localhost:8000"
WAGTAILAPI_BASE_URL = f"http://{WAGTAILADMIN_BASE_URL}"
