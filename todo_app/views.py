from django.shortcuts import render
from django.shortcuts import  render, redirect
from .models import Task
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        if 'task' in request.POST:
            task = request.POST['task']
            if len(task)>0:
                to_do = Task(task = task)
                to_do.save()
                return redirect('home')
            else:
                messages.warning(request, "Please enter a task and try again!")
                return redirect('home')

        


        elif 'second_submit' in request.POST:
            task_id = request.POST['task_id']
            del_task = Task.objects.get(id=task_id)
            print(f"Deleting task: {del_task}")
            del_task.delete()
            return redirect('home')
        
    all_task = Task.objects.all()
    params = {"task":all_task}
    return render(request, "todo_app/index.html",params)
