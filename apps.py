# coding: utf-8

from __future__ import print_function, unicode_literals, division

from django.apps import AppConfig
from django.db.models.signals import post_migrate

from {{ app_name }}.post_migrate import post_migrate_{{ app_name }}


class DefaultConfig(AppConfig):
    name = '{{ app_name }}'
    verbose_name = '{{ app_name }}'

    def ready(self):
        # импортировать сигналы для их регистрации
        import {{ app_name }}.signals
        post_migrate.connect(post_migrate_{{ app_name }}, sender=self)
