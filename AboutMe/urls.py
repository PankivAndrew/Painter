from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.about_me, name='views.about_me'),
]
