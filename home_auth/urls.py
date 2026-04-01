from django.contrib import admin
from django.urls import path,include
from.  import views
urlpatterns=[
     path('signup/', views.signup_view,name='signup'),
     path('login/',views.login_view,name='login'),
     path('logout/',views.logout_view,name='logout'),
     path('forgot-password/', views.forgot_password_view, name='forgot-password'),
     path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
     path('users/', views.user_list, name='user_list'),
     path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
]
