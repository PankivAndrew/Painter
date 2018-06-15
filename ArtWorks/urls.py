from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.main_page, name='views.main_page'),
    url(r'^about/', views.about, name='views.about'),
    url(r'^lectures/', views.lectures, name='views.lectures')
]
