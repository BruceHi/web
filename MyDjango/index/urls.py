from django.urls import path, re_path, register_converter
from . import views, converters

register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')


urlpatterns = [
    path('', views.index),

    # 变量匹配
    path('<int:year>', views.year),  # year
    # path('<int:year>/<str:name>', views.name),  # views.name 表示函数，多个参数用关键字表示

    # 正则表达式匹配，只要接下来的参数符号 4位数字 + .html 就能匹配，再后面加别的东西也能匹配。
    # 比如：http://127.0.0.1:8000/1257.html374 也可以匹配。
    # 传递正则表达式必须要使用**捕获组**。可以是命名的，也可以是非命名的。
    # 若不适用捕获组，则获取不到参数，myyear() missing 1 required positional argument: 'year'
    # 参数就是捕获组获取到的内容。
    # re_path('(\d{4}.html)', views.myyear),  # 结果，比如 1257.html
    re_path('(\d{4}).html', views.myyear, name='urlyear'),  # 结果，比如 1257

    # 自定义过滤器
    path('<yyyy:year>', views.year),

    path('books', views.books),
]
