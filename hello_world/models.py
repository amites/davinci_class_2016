from __future__ import unicode_literals

from datetime import datetime

from django.db import models


RATING_VALUES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), )


class StuffToRate(models.Model):
    """
    This is a collection of things that cna be rated.
    It exists to service an an example of how to create a model that will
    be referenced from other models.
    """
    title = models.CharField(max_length=250)
    color = models.CharField(max_length=100, default='Green')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'StuffToRate - {} - {}'.format(self.title, self.color)

    def get_rating(self):
        if not self.rating_set.count():
            return 'No ratings for {}'.format(self.title)
        total = 0
        for rate in self.rating_set.all():
            total += rate.rating
        return total / self.rating_set.count()


class Rating(models.Model):
    stuff = models.ForeignKey(StuffToRate)
    rating = models.IntegerField(default=1, choices=RATING_VALUES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'Rating -- {} -- {} -- {}'.format(self.stuff.title, self.rating,
                                                 self.stuff.color)


