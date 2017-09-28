from __future__ import unicode_literals

from django.db import models


class Cup(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Round(models.Model):
    name = models.CharField(max_length=50)
    cup = models.ForeignKey('cups.Cup')
    slug = models.SlugField(max_length=50)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __unicode__(self):
        return u'{}, {}'.format(self.name, self.cup.name)
