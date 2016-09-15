from __future__ import unicode_literals

from datetime import datetime

from django.db import models


RATING_VALUES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), )


class StuffToRate(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_rating(self):
        total = 0
        for rate in self.rating_set.all():
            total += rate.rating
        return total / self.rating_set.count()


class Rating(models.Model):
    stuff = models.ForeignKey(StuffToRate)
    rating = models.IntegerField(default=1, choices=RATING_VALUES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
