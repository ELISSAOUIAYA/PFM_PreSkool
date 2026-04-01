from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable_list, name='timetable_list'),
    path('add/', views.timetable_add, name='timetable_add'),
    path('edit/<int:pk>/', views.timetable_edit, name='timetable_edit'),
]