from django.conf.urls import url
from . import views
# The URL pattern that the project calls, now points to index. 
app_name = "app"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
