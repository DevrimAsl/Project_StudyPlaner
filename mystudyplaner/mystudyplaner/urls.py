from django.contrib import admin
from django.urls import path, include
from basic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view),  # 👈 Start = Login
    path('', include('basic.urls')),
]