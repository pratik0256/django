
from django.urls import path
from .views import trigger_background_task

urlpatterns = [
    path('trigger-task/', trigger_background_task, name='trigger_background_task'),
]
