from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('list/', views.teacher_list, name='teacher_list'),
    path('add/', views.add_teacher, name='add_teacher'),
    path('edit/<int:pk>/', views.edit_teacher, name='edit_teacher'),
    path('delete/<int:pk>/', views.delete_teacher, name='delete_teacher'),
]
