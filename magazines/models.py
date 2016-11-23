from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.conf import settings


class Magazine(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases')
    magazine = models.ForeignKey(Magazine)
    subscription_end = models.DateTimeField(blank=True, null=True)  # this is the warning
