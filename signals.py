# coding: utf-8

from __future__ import print_function, unicode_literals, division

from django.db.models import signals
from django.dispatch import receiver

from {{ app_name }} import services, tasks


#@receiver(signals.post_save, sender=Model)
#def function():
#    pass
