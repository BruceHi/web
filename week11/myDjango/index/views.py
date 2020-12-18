from django.shortcuts import render
from django.http import HttpResponse
from .form import LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
   return HttpResponse('Hello Django!')


# 与导入的函数 login 做区分
def login2(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])  # 必须是关键字参数
            if user:
                login(request, user)
                return HttpResponse('登陆成功')
            else:
                return HttpResponse('登陆失败')
    else:
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

