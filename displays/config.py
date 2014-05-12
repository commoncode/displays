from django.apps import AppConfig
from django.utils.importlib import import_module


class DisplayConfig(AppConfig):
    name = 'displays'
    verbose_name = 'Displays'

    def ready(self):
        import_module('displays.collections')
