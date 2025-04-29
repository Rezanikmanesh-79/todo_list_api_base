from django.shortcuts import render
from tasks.models import Task

def remove_completed_tasks(request):
    Task.objects.filter(is_completed=True).delete()
    print('done sending email')
    return "Done"