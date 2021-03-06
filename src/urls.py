"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import main, create_task, get_tasks, edit_task, delete_task,\
    task_up_down, mr_redirect, task_completed, filter_by_priority
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('create/', create_task, name='create_task'),
    path('get/', get_tasks, name='get_tasks'),
    path('edit/<int:task_id>', edit_task, name='edit_task'),
    path('delete/<int:task_id>', delete_task, name='delete_task'),
    path('up_down/<int:task_id>/<str:button>', task_up_down, name='task_up_down'),
    path('completed/<int:task_id>', task_completed, name='task_completed'),
    path('redirect/<int:task_id>', mr_redirect, name='mr_redirect'),
    path('filter_by_priority/', filter_by_priority, name='filter_by_priority'),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
