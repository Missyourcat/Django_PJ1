"""
URL configuration for djangoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tkinter.font import names

from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.views.static import serve

import Helloworld.views
from djangoWeb import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', Helloworld.views.index),
    path('redirectTo', RedirectView.as_view(url='index/')),
    path('blog/<int:id>', Helloworld.views.blog),
    path('blog2/<int:year>/<int:month>/<int:day>/<int:id>', Helloworld.views.blog2),
    re_path('blog3/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})', Helloworld.views.blog3),
    # 配置媒体文件的路由地址
    # re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media')
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('order/', include(('order.urls', 'order'), namespace='order')),
    path('download1/', Helloworld.views.download_file1),
    path('download2/', Helloworld.views.download_file2),
    path('download3/', Helloworld.views.download_file3),
    path('get/', Helloworld.views.get_test),
    path('post/', Helloworld.views.post_test),
    path('tologin/', Helloworld.views.to_login),
    path('login/', Helloworld.views.login),
    path('toupload/', Helloworld.views.to_upload),
    path('upload', Helloworld.views.upload),
    path('student/list', Helloworld.views.List.as_view()),
    # path('student/<int:pk>', Helloworld.views.Detail.as_view()),
    path('student/<int:id>', Helloworld.views.Detail.as_view()),
    path('student/create', Helloworld.views.Create.as_view()),
    path('student/update/<int:pk>', Helloworld.views.Update.as_view()),
    path('student/delete/<int:pk>', Helloworld.views.Delete.as_view()),

]
