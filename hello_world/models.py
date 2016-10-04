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


#####################


class Customer(models.Model):
    human_first_name = models.CharField(max_length=250)
    human_last_name = models.CharField(max_length=250)
    mileage = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return '{} {}'.format(self.human_first_name, self.human_last_name)


class Pet(models.Model):
    name = models.CharField(max_length=200, default='Katie')
    breed = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, default=1)

    def __unicode__(self):
        return 'Pet Name : {} belongs to : {} {}'.format(
            self.name, self.customer.human_first_name,
            self.customer.human_last_name)

    def __str__(self):
        return self.__unicode__()


class Service(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name


class Order(models.Model):
    # customer should be linked to Pet in production
    customer = models.ForeignKey(Customer)
    service = models.ManyToManyField(Service)


# class OrderToService(models.Model):
#     """
#     Example of how a ManyToMany field works at the database level.
#     """
#     order = models.ForeignKey(Order)
#     service = models.ForeignKey(Service)
