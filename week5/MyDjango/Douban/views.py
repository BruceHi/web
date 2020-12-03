from django.shortcuts import render

# Create your views here.
from .models import T1
from django.db.models import Avg


def books_short(request):

    # 完整数据 QuerrySet 对象
    shorts = T1.objects.all()

    # 评论数量
    counter = shorts.count()

    # 平均星级
    star_avg = f" {shorts.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # star_avg, = shorts.aggregate(Avg('n_star')).values()

    # dic.values() 方法产生的类型是 dict_values，不能通过索引取得结果，即使里面只有一个元素。
    # dict_values([2])
    # TypeError: 'dict_values' object does not support indexing
    # print('{:0.1f}'.format(shorts.aggregate(Avg('sentiment')).values()[0]))

    # 双下划线
    sent_avg = '{:0.1f}'.format(shorts.aggregate(Avg('sentiment'))['sentiment__avg'])

    # 正向数量 大于等于0.5
    plus = shorts.filter(sentiment__gte=0.5).count()

    # 负向数量
    # minus = counter - plus
    minus = shorts.filter(sentiment__lt=0.5).count()

    return render(request, 'result.html', locals())
