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
import json

# The Generic View that now relies on Angular to do the rest.
class IndexView(generic.TemplateView):
  template_name = 'index.html'

# New User Registration (Interacts with the registration partial, js, and models.py --Some files are currently being renamed, Sorry I can't be more specific.)
def createUser(request):
    data = json.loads(request.body.decode())


    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    username = data['username']
    password = data['password']
    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        username=username,
        password=password
    )

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

# @csrf_exempt
def login(request):
    data = json.loads(request.body.decode())
    username = data['username']
    password = data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        login(request)
        return HttpResponseRedirect('/#/tixit')
    else:
        return  render(request, 'auth_lifecycle/user_profile.html',
        context_instance=RequestContext(request))
        # No backend authenticated the credentials
        # EOFError


# New Event Creation (Interacts with new_event.html and new_event.js. And models.py.)
# @csrf_exempt
def new_event(request):
    data = json.loads(request.body.decode())

    eventname = data['eventname']
    eventdescription = data['eventdescription']
    city = data['eventcity']
    eventvenue = data['eventvenue']
    limit = data['eventattendeelimit']
    startdate = data['eventstartdate']
    enddate = data['eventenddate']
    startdate = datetime.datetime.strptime(startdate, '%m/%d/%y')
    enddate = datetime.datetime.strptime(enddate, '%m/%d/%y')
    event = Event.objects.create(
        name = eventname,
        description = eventdescription,
        city = city,
        venueName = eventvenue,
        limit = limit,
        startDate = startdate,
        endDate = enddate
    )

    event.save()
    return HttpResponseRedirect('/#/new_event_conf/')

@csrf_exempt
def all_events():
    pass
