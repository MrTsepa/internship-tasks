from __future__ import unicode_literals

from django.apps import AppConfig


class ProblemsConfig(AppConfig):
    name = 'problems'

    def ready(self):
        import signals
