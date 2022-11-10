from unicodedata import name
from django.contrib import admin

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('project', views.project, name='project'),
    path('blog', views.blog, name='blog'),
    path('single', views.single, name='single'),
    path('booking', views.booking, name='booking'),
    path('feedback', views.feedback, name='feedback'),

   
   


    # path('saveform', views.saveform, name='saveform')

    path('saveenquiry/', views.saveEnquiry, name="saveenquiry")
]
