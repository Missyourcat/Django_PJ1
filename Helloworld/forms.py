from django import forms
from django.forms import ModelForm

from Helloworld.models import Student


# 定义学生form表单
class StudentForm(ModelForm):
    class Meta:  # 配置中心
        model = Student  # 导入model
        fields = '__all__'  # 代表所有字段
        # fields = ['name']  # 代表某些字段

        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'class': 'inputClass'}),
            'age': forms.TextInput(attrs={'id': 'age'}),
        }

        # 指定标签
        labels = {
            'name': '姓名',
            'age': '年龄'
        }
