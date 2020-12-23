'''Creating a new urls.py file inside the application folder'''
from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index, name='index'),
]
