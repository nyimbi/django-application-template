# coding: utf-8

from __future__ import print_function, unicode_literals, division

try:
    from celery.task import task
except ImportError:
    pass
