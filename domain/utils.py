import hashlib
from abc import ABCMeta
from typing import Type, List, Dict

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Model
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


def md5(s: str) -> str:
    md5_obj = hashlib.md5(settings.SECRET_KEY.encode("utf-8"))
    md5_obj.update(s.encode("utf-8"))
    return md5_obj.hexdigest()


class CommonView(metaclass=ABCMeta):
    GET = "GET"

    def __init__(self, model: Type[Model], model_form: Type[ModelForm], **kwargs):
        self.model = model
        self.model_form = model_form
        self.limit = kwargs.get("limit", 10)
        self.list_title = kwargs.get("list_title", "列表")
        self.add_title = kwargs.get("add_title", "添加")
        self.edit_title = kwargs.get("edit_title", "修改")

    def list(self, request):
        title = self.list_title
        index = int(request.GET.get("index", 1))
        fields = self._get_fields()
        page = Paginator(self._object_mapper(), self.limit).page(index)
        return render(request, "list.html", locals())

    def update(self, request):
        title = self.add_title
        object_id = request.GET.get("id")
        instance = None
        if object_id is not None:  # 更新操作
            title = self.edit_title
            instance = self.model.objects.filter(id=object_id).first()
        if request.method == CommonView.GET:
            form = self.model_form(instance=instance)
            return render(request, "update.html", locals())
        form = self.model_form(instance=instance, data=request.POST)
        if not form.is_valid():
            return render(request, "update.html", locals())
        form.save()
        return HttpResponseRedirect("list")

    def delete(self, request):
        object_id = request.GET.get("id")
        if object_id is not None:
            self.model.objects.filter(id=object_id).delete()
        return HttpResponseRedirect("list")

    def _get_fields(self) -> List[str]:
        return [x.verbose_name for x in self.model._meta.fields]

    def _object_mapper(self) -> List[Dict[str, object]]:
        object_list = []
        for obj in self.model.objects.all().order_by():
            copy = obj.__dict__.copy()
            copy.pop("_state")
            object_list.append(copy)
        return object_list
