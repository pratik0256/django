
from django.shortcuts import render
from .tasks import my_background_task

def trigger_background_task(request):

    my_background_task.delay()

    return render(request, 'myrqapp/task_triggered.html')
