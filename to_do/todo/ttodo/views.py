from django.shortcuts import render, redirect
from .models import Task
from datetime import datetime, timedelta

def task_list(request):
    tasks = Task.objects.filter(completed=False).order_by('deadline', '-priority')
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        deadline = request.POST.get('deadline')
        priority = request.POST.get('priority', 1)
        
        new_task = Task(
            title=title,
            description=description,
            deadline=deadline,
            priority=priority
        )
        new_task.save()
        return redirect('task_list')
    return render(request, 'add_task.html')
