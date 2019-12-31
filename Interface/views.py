from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from Interface.models import Event


def list(request):
    return render(request, "list.html")


@csrf_exempt
def add_event(request):

    if request.is_ajax():
        print(request.body)
        print(request.POST)

        name = request.POST.get('name', '')  # 发布会名称
        print(name)
        limit = request.POST.get('limit', '')  # 限制人员
        print(limit)
        status = request.POST.get('status', '')  # 发布会状态
        address = request.POST.get('address', '')  # 发布会地址
        start_time = request.POST.get('start_time', '')  # 发布会开始日期
        create_time = request.POST.get('create_time', '')  # 发布会创建日期

        if name == '' or limit == '' or status == '' or start_time == '' or create_time == '':
            return JsonResponse({'status': 10021, 'message': 'parameter is null'})

        # 判断发布会名称重复
        result = Event.objects.filter(name=name)
        if result:
            return JsonResponse({'status': 10023, 'message': 'event name already exists'})

        if status == '':
            status = 1

        try:
            Event.objects.create(name=name, limit=limit, address=address, status=int(status), start_time=start_time,
                                 create_time=create_time)
        except ValidationError as e:
            error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS'
            return JsonResponse({'status': 10024, 'message': error})
        return JsonResponse({'status': 200, 'message': 'add event success'})
