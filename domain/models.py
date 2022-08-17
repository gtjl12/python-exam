from django.db.models import Model, AutoField, CharField, SmallIntegerField, DateField, ForeignKey, CASCADE

gender_choices = (
    (0, '女'),
    (1, '男'),
)


class Administrator(Model):
    id = AutoField(verbose_name="编号", primary_key=True)
    username = CharField(verbose_name="用户名", max_length=32, unique=True)
    password = CharField(verbose_name="密码", max_length=32)


class Classes(Model):
    id = AutoField(verbose_name="编号", primary_key=True)
    name = CharField(verbose_name="名称", max_length=32)

    def __str__(self):
        return self.name


class Student(Model):
    id = AutoField(verbose_name="编号", primary_key=True)
    name = CharField(verbose_name="姓名", max_length=32)
    gender = SmallIntegerField(verbose_name="性别", choices=gender_choices)
    age = SmallIntegerField(verbose_name="年龄")
    entry_time = DateField(verbose_name="入学时间")
    classes = ForeignKey(verbose_name="班级", to=Classes, on_delete=CASCADE)
