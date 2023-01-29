from django.urls import path
from . import views

# defines our routes, points our routes to the templates we have created in the views file
urlpatterns = [
    path('', views.home, name='blogs-home'),
    path('about/', views.about, name='blogs-about'),
]