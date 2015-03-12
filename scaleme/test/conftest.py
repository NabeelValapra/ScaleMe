# -*- coding: utf-8 -*-
# Standard Library
import os

# Third Party Stuff
import django
# import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.test")


def pytest_configure(config):
    django.setup()