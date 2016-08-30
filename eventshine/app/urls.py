from django.conf.urls import url
from . import views
# The URL pattern that the project calls, now points to index.
app_name = "app"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^createUser/$', views.createUser, name='createUser'),
    url(r'^new_event/$', views.new_event, name='new_event'),
]
