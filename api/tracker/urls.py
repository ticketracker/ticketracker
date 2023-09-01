from django.urls import path
from . import views


app_name = 'tracker'


urlpatterns = [
    path('v1/tracker', views.api_create_tracker, name='api_create_tracker'),
]