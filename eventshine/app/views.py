from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import *
import datetime

# The Generic View that now relies on Angular to do the rest.
class IndexView(generic.TemplateView):
  template_name = 'index.html'

# New User Registration (Interacts with the registration partial, js, and models.py --Some files are currently being renamed, Sorry I can't be more specific.)
@csrf_exempt
def createUser(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(first_name=firstname, last_name=lastname,
                                    email=email, username=username, password=password)
    user.save()
    return HttpResponseRedirect('/#/')
    # user = authenticate(username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     # Redirect to a success page.
    #     ...
    # else:
    #     # Return an 'invalid login' error message.
    #     ...

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username, password)
    if user is not None:
        # A backend authenticated the credentials
        login(username=username, password=password)
        return HttpResponseRedirect('/#/tixit')


    else:
        # No backend authenticated the credentials
        EOFError
# New Event Creation (Interacts with new_event.html and new_event.js. And models.py.)
@csrf_exempt
def new_event(request):
    eventname = request.POST['eventname']
    eventdescription = request.POST['eventdescription']
    city = request.POST['city']
    eventvenue = request.POST['eventvenue']
    limit = request.POST['limit']
    startdate = request.POST['startdate']
    enddate = request.POST['enddate']
    startdate = datetime.datetime.strptime(startdate, '%m/%d/%y')
    enddate = datetime.datetime.strptime(enddate, '%m/%d/%y')


    event = Event.objects.create(name=eventname, description=eventdescription, city=city, venueName=eventvenue, limit=limit, startDate=startdate, endDate=enddate)
    event.save()
    return HttpResponseRedirect('/#/new_event_conf/')

@csrf_exempt
def all_events():
    pass
