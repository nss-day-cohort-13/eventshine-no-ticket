from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from django.core import serializers

# The Generic View that now relies on Angular to do the rest.
class IndexView(generic.TemplateView):
  template_name = 'index.html'
