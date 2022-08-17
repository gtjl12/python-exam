from abc import ABCMeta, abstractmethod

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class MiddlewareMixinBase(MiddlewareMixin, metaclass=ABCMeta):
    @abstractmethod
    def process_request(self, request: HttpRequest):
        ...

    @abstractmethod
    def process_response(self, request: HttpRequest, response: HttpResponse):
        ...


class AdministratorAuth(MiddlewareMixinBase):
    def process_request(self, request):
        path = request.path_info
        info = request.session.get("info")
        if path != "/login/in" and info is None:
            return HttpResponseRedirect("/login/in")
        elif path == "/login/in" and info is not None:
            return HttpResponseRedirect("/administrator/list")

    def process_response(self, request: HttpRequest, response: HttpResponse):
        return response
