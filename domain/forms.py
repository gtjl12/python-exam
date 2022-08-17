from django.forms import Form, Field, ModelForm, CharField, PasswordInput, ValidationError, DateInput

from domain.models import Administrator, Classes, Student
from domain.utils import md5


class FormBase(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            name: str
            field: Field
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = field.label


class ModelFormBase(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            name: str
            field: Field
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = field.label


class AdministratorModelForm(ModelFormBase):
    confirm_password = CharField(label="确认密码", widget=PasswordInput(render_value=True))

    class Meta:
        model = Administrator
        fields = "__all__"
        widgets = {
            "password": PasswordInput(render_value=True)
        }

    def clean_password(self):
        return md5(self.cleaned_data.get("password"))

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = md5(self.cleaned_data.get("confirm_password"))
        if password != confirm_password:
            raise ValidationError("密码和确认密码不一致")
        return confirm_password


class AdministratorLoginForm(FormBase):
    username = CharField(label="用户名")
    password = CharField(label="密码", widget=PasswordInput(render_value=True))

    def clean_password(self):
        return md5(self.cleaned_data.get("password"))


class ClassesModelForm(ModelFormBase):
    class Meta:
        model = Classes
        fields = "__all__"


class StudentModelForm(ModelFormBase):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "entry_time": DateInput(attrs={"type": "date"}, format="%Y-%m-%d")
        }
