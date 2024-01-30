
from django_rq import job
import time

@job
def my_background_task():

    time.sleep(5)
    print("Background task completed!")
