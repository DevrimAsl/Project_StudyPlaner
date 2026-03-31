from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task, Subject

# Home
def home(request):
    return render(request, 'home.html')


# Registrierung
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# Dashboard
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    subjects = Subject.objects.filter(user=request.user)

    completed = tasks.filter(completed=True).count()
    total = tasks.count()

    progress = 0
    if total > 0:
        progress = int((completed / total) * 100)

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'subjects': subjects,
        'progress': progress
    })


# Fach erstellen
@login_required
def add_subject(request):
    if request.method == 'POST':
        name = request.POST['name']
        Subject.objects.create(name=name, user=request.user)
        return redirect('dashboard')

    return render(request, 'addSubject.html')


# Aufgabe erstellen
@login_required
def add_task(request):
    subjects = Subject.objects.filter(user=request.user)

    if request.method == 'POST':
        Task.objects.create(
            title=request.POST['title'],
            subject=Subject.objects.get(id=request.POST['subject']),
            due_date=request.POST['due_date'],
            study_time=request.POST['study_time'],
            user=request.user
        )
        return redirect('dashboard')

    return render(request, 'addTask.html', {'subjects': subjects})


# Aufgabe erledigt
@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('dashboard')