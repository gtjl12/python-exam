"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from domain.views import AdministratorView, ClassesView, StudentView

administrator_view = AdministratorView()
classes_view = ClassesView()
student_view = StudentView()

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', administrator_view.login_in),
    path('login/in', administrator_view.login_in),
    path('login/out', administrator_view.login_out),

    path('administrator/list', administrator_view.list),
    path('administrator/update', administrator_view.update),
    path('administrator/delete', administrator_view.delete),

    path('classes/list', classes_view.list),
    path('classes/update', classes_view.update),
    path('classes/delete', classes_view.delete),

    path('student/list', student_view.list),
    path('student/update', student_view.update),
    path('student/delete', student_view.delete),
]
