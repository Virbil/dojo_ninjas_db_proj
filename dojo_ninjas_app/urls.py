from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('submit-dojo', views.submit_dojo),
    path('submit-ninja', views.submit_ninja),
]