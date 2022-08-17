from typing import List, Dict

from django.http import HttpResponseRedirect
from django.shortcuts import render

from domain.forms import AdministratorModelForm, AdministratorLoginForm, StudentModelForm, ClassesModelForm
from domain.models import Administrator, Student, Classes
from domain.utils import CommonView


class AdministratorView(CommonView):
    def __init__(self):
        super().__init__(Administrator, AdministratorModelForm, **{
            "list_title": "管理员列表",
            "add_title": "添加管理员",
            "edit_title": "修改员列表",
        })

    def _object_mapper(self) -> List[Dict[str, object]]:
        object_list = []
        for obj in self.model.objects.all().order_by():
            obj: Administrator
            object_list.append({
                "id": obj.id,
                "username": obj.username,
                "password": "******"
            })
        return object_list

    def login_in(self, request):
        if request.method == CommonView.GET:
            form = AdministratorLoginForm()
            return render(request, "login.html", locals())
        form = AdministratorLoginForm(data=request.POST)
        if not form.is_valid():
            return render(request, "login.html", locals())
        admin = Administrator.objects.filter(**form.cleaned_data).first()
        if admin is None:
            form.add_error("username", "用户名或密码错误")
            form.add_error("password", "用户名或密码错误")
            return render(request, "login.html", locals())
        request.session["info"] = {**form.cleaned_data}
        return HttpResponseRedirect("/administrator/list")

    def login_out(self, request):
        request.session.flush()
        return HttpResponseRedirect("/login/in")


class ClassesView(CommonView):
    def __init__(self):
        super().__init__(Classes, ClassesModelForm, **{
            "list_title": "班级列表",
            "add_title": "添加班级",
            "edit_title": "修改班级",
        })


class StudentView(CommonView):
    def __init__(self):
        super().__init__(Student, StudentModelForm, **{
            "list_title": "学生列表",
            "add_title": "添加学生",
            "edit_title": "修改学生",
        })

    def _object_mapper(self) -> List[Dict[str, object]]:
        object_list = []
        for obj in self.model.objects.all().order_by():
            obj: Student
            object_list.append({
                "id": obj.id,
                "name": obj.name,
                "gender": obj.get_gender_display(),
                "age": obj.age,
                "entry_time": obj.entry_time.strftime("%Y-%m-%d"),
                "classes": obj.classes.name
            })
        return object_list
