from django.urls import path
from user_app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('careers', careers, name='careers'),
    path('courses', courses, name='courses'),
    path('placements', placements, name='placements'),
    path('contact', contact, name='contact'),
]