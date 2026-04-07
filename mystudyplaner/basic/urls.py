from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),   # Startseite → Login
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-subject/', views.add_subject, name='add_subject'),
    path('add-task/', views.add_task, name='add_task'),
    path('complete-task/<int:task_id>/', views.complete_task, name='complete_task'),
]