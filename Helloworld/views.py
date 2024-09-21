import os.path

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, StreamingHttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from Helloworld.forms import StudentForm
from Helloworld.models import Student


# Create your views here.
def index(request):
    # str = '模板引擎'
    # content_value = {'msg': str}
    # return render(request, 'index.html', content_value)
    return render(request, 'http.html')

    # return redirect('/static/new.html', permanent=False)
    # content_value = {'msg': 'hello'}
    # return render(request, 'index2.html', context=content_value)

    # return JsonResponse({'foo': 'bar'})

    # return HttpResponseNotFound()

    # html = "<font color='blue'>Hello World</font>"
    # return HttpResponse(html, status=200)

    # return redirect('/static/new.html', permanent=True)
    # return redirect('/blog/2')

    # return HttpResponseNotFound()

    # print("请求处理中、")
    # return render(request, 'index.html')


# def blog(request, id):
#     return HttpResponse(f"id是{str(id)}的博客页面")

def blog(request, id):
    if id == 0:
        return redirect('/static/error.html')
    else:
        return HttpResponse(f"id是{str(id)}的博客页面")


def blog2(request, year, month, day, id):
    return HttpResponse(f'{str(year)}/{str(month)}/{str(day)}/id是{str(id)}')


def blog3(request, year, month, day):
    return HttpResponse(f'{str(year)}/{str(month)}/{str(day)}')


# 定义文件路径
file_path = 'D:\Code\python\DjangoProject\djangoWeb\common\cloudmusic.exe'


def download_file1(request):
    file = open(file_path, 'rb')  # 打开文化
    response = HttpResponse(file)  # 创建HttpResponse对象
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="test1.exe"'
    return response


def download_file2(request):
    file = open(file_path, 'rb')  # 打开文化
    response = StreamingHttpResponse(file)  # 创建StreamingHttpResponse对象
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="test2.exe"'
    return response


def download_file3(request):
    file = open(file_path, 'rb')  # 打开文化
    response = FileResponse(file)  # 创建FileResponse对象
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="test3.exe"'
    return response


def get_test(request):
    """
    get请求测试
    :param request:
    :return:
    """
    print(request.method)  # 请求方法
    # 常用属性
    print(request.content_type)
    print(request.content_params)
    print(request.COOKIES)
    print(request.scheme)
    # 常用方法
    print(request.is_secure())
    print(request.get_host())
    print(request.get_full_path())

    print(request.GET.get('name'))
    print(request.GET.get('pwd'))
    print(request.GET.get('aaa', '666'))

    return HttpResponse('get')


def post_test(request):
    """
    post请求参数
    :param request:
    :return:
    """
    print(request.POST.get('name'))
    print(request.POST.get('pwd'))
    print(request.POST.get('aaa', '666'))
    return HttpResponse('post')


def to_login(request):
    """
    跳转登录页面
    :param request:
    :return:
    """
    return render(request, 'login.html')


def login(request):
    """
    登录
    :param request:
    :return:
    """
    user_name = request.POST.get('user_name')
    user_password = request.POST.get('user_pwd')
    # print(user_name, user_password)
    if user_name == 'user' and user_password == '123456':
        request.session['currentUserName'] = user_name  # session中存一个用户名
        print('session获取:', request.session['currentUserName'])
        response = render(request, 'main.html')
        response.set_cookie('rememeber_me', True)
        return response
    else:
        context_value = {'error_info': '用户名或密码错误'}
        return render(request, 'login.html', context_value)


def to_upload(request):
    """
    跳转文件上传文件
    :param request:
    :return:
    """
    return render(request, 'upload.html')


def upload(request):
    """
    文件上传处理
    :param request:
    :return:
    """
    # 获取上传的文件，如果没有文件，默认返回none
    myFile = request.FILES.get('myfile', None)
    if myFile:
        # 打开特定的文件进行二进制写操作
        f = open(os.path.join("D:\Code\python\DjangoProject\djangoWeb\common", myFile.name), 'wb+')
        # 分块写入文件
        for chunk in myFile.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse("文件上传成功")
    else:
        return HttpResponse("没有发现文件")


class List(ListView):
    # 设置模板文件
    template_name = 'student/list.html'
    # 设置模型外的数据
    extra_context = {'title': '学生信息'}
    # 定义结果集
    queryset = Student.objects.all()
    # 设置每页展示的数据条数
    paginate_by = 5
    # 设置上下文对象名称
    context_object_name = 'student_list'


class Detail(DetailView):
    # 设置模板文件
    template_name = 'student/detail.html'
    # 设置模型外的数据
    extra_context = {'title': '学生信息'}
    # 设置查询模型
    model = Student
    # 设置上下文对象名称
    context_object_name = 'student'
    # 指定URL中用于获取对象的唯一标识符的参数名称，默认'pk'
    pk_url_kwarg = 'id'


class Update(UpdateView):
    # 设置模板文件
    template_name = 'student/update.html'
    # 设置模型外的数据
    extra_context = {'title': '学生信息修改'}
    # 设置查询模型
    model = Student
    # 指定form表单
    form_class = StudentForm
    # 执行完成后跳转地址
    success_url = '/student/list'


class Create(CreateView):
    # 设置模板文件
    template_name = 'student/create.html'
    # 设置模型外的数据
    extra_context = {'title': '学生信息新增'}
    # 指定form表单
    form_class = StudentForm
    # 执行完成后跳转地址
    success_url = '/student/list'


class Delete(DeleteView):
    # 设置模板文件
    template_name = 'student/delete.html'
    # 设置模型外的数据
    extra_context = {'title': '学生信息修改'}
    # 设置查询模型
    model = Student
    # 设置上下文对象名称
    context_object_name = 'student'
    # 执行完成后跳转地址
    success_url = '/student/list'
