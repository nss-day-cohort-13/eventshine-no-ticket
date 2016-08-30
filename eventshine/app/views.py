from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


# The Generic View that now relies on Angular to do the rest.
class IndexView(generic.TemplateView):
  template_name = 'index.html'

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
    user = authenticate(username=username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        login(username=username, password=password)
        return HttpResponseRedirect('/#/tixit')


    else:
        # No backend authenticated the credentials
        EOFError
