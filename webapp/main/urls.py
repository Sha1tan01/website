from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    #path('profile', profile_view, name="profile")
]