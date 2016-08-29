from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# These are the tables for our database
# Event Table
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    venueName = models.CharField(max_length=200)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    limit = models.IntegerField()

# Venue Table...ok, you get the idea.
class Venue(models.Model):
    # venueID = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    eventID = models.ForeignKey('Event', on_delete=None)

# class User(models.Model):
#     userID = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     paymentName = models.CharField(max_length=200)
#     paymentNumber = models.CharField(max_length=200)
#     password = models.CharField(max_length=100)

class EventUser(models.Model):
    # eventUserID = models.CharField(max_length=200)
    eventID = models.ForeignKey('Event', on_delete=None)
    userID = models.ForeignKey(User, on_delete=None)
