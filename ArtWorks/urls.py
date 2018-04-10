from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.main_page, name='main_page'),
]
