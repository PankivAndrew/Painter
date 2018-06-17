from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.art_works, name='views.art_works'),
    url(r'^about/', views.about, name='views.about'),
    # url(r'^lectures/', views.lectures, name='views.lectures')
]
