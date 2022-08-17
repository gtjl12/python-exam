# 学生管理系统

---

## 一.环境

* python3.9
* django3.2.5
* docker1.13.1
* centos7

## 二.设计

### 数据库

|      表名       |     字段     |     描述      |
|:-------------:|:----------:|:-----------:|
| administrator |     id     |   主键 自动增长   |
| administrator |  username  | varchar(32) |
| administrator |  password  | varchar(32) |
|    classes    |     id     |   主键 自动增长   |
|    classes    |    name    | varchar(32) |
|    student    |     id     |   主键 自动增长   |
|    student    |    name    | varchar(32) |
|    student    |   gender   |   integer   |
|    student    |    age     |   integer   |
|    student    | entry_time |    date     |
|    student    | classes_id |  外键 级联更新删除  |

### 前端

|           名称           |          功能          |       描述        |
|:----------------------:|:--------------------:|:---------------:|
|      _layout.html      |         模板页面         |      模板页面       |
|       list.html        |       展示/删除数据        | 继承_layout.html  |
|      update.html       |       添加/修改数据        | 继承_layout.html  |
|       login.html       |        管理员登录         | 继承_layout.html  |
|        FormBase        |   bootstrap样式Form    |     继承Form      |
| AdministratorLoginForm |       管理员登录表单        |   继承FormBase    |
|     ModelFormBase      | bootstrap样式ModelForm |   继承ModelForm   |
| AdministratorModelForm |       管理员添加/修改       | 继承ModelFormBase |
|    ClassesModelForm    |       班级添加/修改        | 继承ModelFormBase |
|    StudentModelForm    |       学生添加/修改        | 继承ModelFormBase |

### 视图

|         名称          |     功能      |        描述         |
|:-------------------:|:-----------:|:-----------------:|
|     CommonView      | 提供通用的CRUD方法 |     通用CRUD视图      |
|  AdministratorView  |   管理员增删改    |       登录登出        |	继承CommonView
|     ClassesView     |    班级增删改    |   继承CommonView    |
|     StudentView     |    学生增删改    |   继承CommonView    |
| MiddlewareMixinBase |    抽象中间件    | 继承MiddlewareMixin |
|  AdministratorAuth  |    身份验证     |      拦截未登录请求      |	继承MiddlewareMixinBase

## 三.运行

```bash
sudo yum install -y docker
sudo systemctl enable docker
sudo systemctl start docker
...
sudo docker build -t exam:1.0 .
sudo docker images
sudo docker run --name exam -d exam:1.0 -p 8080:8080
sudo docker ps
```