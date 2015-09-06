# coding: utf-8

from django.apps import AppConfig


class DefaultConfig(AppConfig):
    name = '{{ app_name }}'
    verbose_name = '{{ app_name }}'

    def ready(self):
        # импортировать сигналы для их регистрации
        import {{ app_name }}.signals
