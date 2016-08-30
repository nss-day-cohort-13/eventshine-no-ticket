from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from .models import *
import datetime
import json

# The Generic View that now relies on Angular to do the rest.
class IndexView(generic.TemplateView):
  template_name = 'index.html'

# New User Registration (Interacts with the registration partial, js, and models.py --Some files are currently being renamed, Sorry I can't be more specific.)
@csrf_exempt
def createUser(request):
    '''
        Function to catch registration of user from login.html.
        Upon form submition, the values of the fields are passed in via the arg 'request'
        and then set to variables below.
        Following we create a user by setting the variables passed in the the create_user function
        below and then we save it to our database.
        Args:
            'request' - the values passed in as string via the form of login.html
    '''

    # print('request', request.POST)
    obj = json.loads(request.body.decode())
    print('obj', obj)
    username =  obj['username']
    password = obj['password']
    email = obj['email']
    first_name = obj['first_name']
    last_name = obj['last_name']

    user = User.objects.create_user(
                                    username=username,
                                    password=password,
                                    email=email,
                                    first_name=first_name,
                                    last_name=last_name,
                                    )

    user.save()
    return HttpResponseRedirect('/')
    # firstname = request.POST['firstname']
    # lastname = request.POST['lastname']
    # email = request.POST['email']
    # username = request.POST['username']
    # password = request.POST['password']
    # user = User.objects.create_user(first_name=firstname, last_name=lastname,
    #                                 email=email, username=username, password=password)
    # user.save()
    # return HttpResponseRedirect('/#/')
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
    user = authenticate(username=username, password=password)
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
    return HttpResponseRedirect('/#/conf/')


# CREATE USER #
# @csrf_exempt
# def create_user_object(request):
