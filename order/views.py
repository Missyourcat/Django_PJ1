# Create your views here.


from django.http import HttpResponse
from django.urls import reverse, resolve


def index(request):
    route_url = reverse('order:index')
    print("reverse反向解析得到的路由地址", route_url)
    result = resolve(route_url)
    print("resolve通过路由地址得到路由信息", str(result))
    return HttpResponse("订单信息")


def list(request, year, month, day):
    # route_url = reverse('order:list')
    # print("reverse反向解析得到的路由地址", route_url)
    # result = resolve(route_url)
    # print("resolve通过路由地址得到路由信息", str(result))
    kwargs = {'year': year, 'month': month, 'day': day}
    args = [year, month, day]
    # route_url = reverse('order:list', kwargs=kwargs)
    route_url = reverse('order:list', args=args)
    print("reverse反向解析得到的路由地址", route_url)
    result = resolve(route_url)
    print("resolve通过路由地址得到路由信息", str(result))
    return HttpResponse('订单列表')
