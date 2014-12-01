# coding: utf-8

from __future__ import print_function, unicode_literals, division

from {{ app_name }} import models


def post_migrate_{{ app_name }}(sender, app_config, verbosity,
                                interactive, using, **kwargs):
    """
    Эта функция будет выполнена после миграции приложения.

    Это альтернатива миграциям данных и фикстурам. Пример:

        models.Model.objects.get_or_create(name=u'Sample object')

    После миграции создаст объект Model(name=u'Sample object').
    """
    pass
