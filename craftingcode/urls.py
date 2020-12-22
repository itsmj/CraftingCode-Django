from django.urls import path
from .import views

urlpatterns=[
    path('', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
    
    ]