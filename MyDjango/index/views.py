from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello Django!')


def year(request, year):
    # return HttpResponse(year)
    return redirect('/2020.html')


def name(request, **kwargs):
    return HttpResponse((kwargs['name'], kwargs['year']))


def myyear(request, year):
    # return HttpResponse(year)

    # Templates 文件夹增加yearview.html
    return render(request, 'yearview.html')

from .models import Name


def books(request):
    n = Name.objects.all()
    return render(request, 'bookslist.html', locals())
