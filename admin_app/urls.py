from django.urls import path
from admin_app.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('course/add/', course_add, name='course-add'),
    path('course/list/', course_list, name='course-list'),
    path('course/<int:course_id>/edit/', course_edit, name='course-edit'),
    path('course/<int:course_id>/delete/', course_delete, name='course-delete'),
]