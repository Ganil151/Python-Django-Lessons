from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'counter', views.counter, name='counter'),
    path(r'register', views.register, name='register'),
    path(r'login', views.login, name='login'),
    path(r'logout', views.logout, name='login'),
    path(r'post/<str:pk>', views.post, name='post'),
]
