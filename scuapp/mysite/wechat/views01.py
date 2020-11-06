from django.shortcuts import HttpResponse,render
from django.utils import timezone
from django.template import loader
from .models import Tbcompany, Tbmanager, Tbstudent,Tbresume, Tbqualify,TbinWork,TboutWork
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

#后台管理界面

#一大波界面导入
#首页
@csrf_exempt
def index(request):
    return render(request, 'wechat/index.html')
#登录界面
@csrf_exempt
def login(request):
    return render(request, 'wechat/login.html')
#校内兼职信息展示界面
@csrf_exempt
def inwork_list(request):
    inwork_list = TbinWork.objects.all()
    return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})

#校内兼职信息发布界面
@csrf_exempt
def inwork_add(request):
    return render(request, 'wechat/inwork_add.html')

#功能接口
#登录
def management_login(request):
    if request.method == "POST":
        iw_post=request.POST.get("IW_post")
        iw_depart=request.POST.get("IW_depart")
        w_time=request.POST.get("W_Time")
        w_place=request.POST.get("W_place")
        work=request.POST.get("Work")
        w_salary=request.POST.get("W_salary")
        w_reuire=request.POST.get("W_require")
        w_amount=request.POST.get("W_amount")
        ddl_time=request.POST.get("Ddl_time")
        inpub_time=timezone.now()
        w_ps=request.POST.get("W_ps")
        inWork=TbinWork.objects.create(iw_post=iw_post, iw_depart=iw_depart, w_time=w_time, w_place=w_place, work=work,
                                       w_salary=w_salary, w_reuire=w_reuire, w_amount=w_amount, ddl_time=ddl_time, inpub_time=inpub_time, w_ps=w_ps)
        inWork.save()
        inwork_list = TbinWork.objects.all()
        return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})
    else:
        return HttpResponse("请求错误")

#校内兼职信息发布
@csrf_exempt
def management_inWork_release(request):
    if request.method == "POST":
        iw_post=request.POST.get("IW_post")
        iw_depart=request.POST.get("IW_depart")
        w_time=request.POST.get("W_Time")
        w_place=request.POST.get("W_place")
        work=request.POST.get("Work")
        w_salary=request.POST.get("W_salary")
        w_reuire=request.POST.get("W_require")
        w_amount=request.POST.get("W_amount")
        ddl_time=request.POST.get("Ddl_time")
        inpub_time=timezone.now()
        w_ps=request.POST.get("W_ps")
        inWork=TbinWork.objects.create(iw_post=iw_post, iw_depart=iw_depart, w_time=w_time, w_place=w_place, work=work,
                                       w_salary=w_salary, w_reuire=w_reuire, w_amount=w_amount, ddl_time=ddl_time, inpub_time=inpub_time, w_ps=w_ps)
        inWork.save()
        inwork_list = TbinWork.objects.all()
        return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})
    else:
        return HttpResponse("请求错误")

#校内兼职信息修改
@csrf_exempt
def management_inWork_reset_show(request):
    iw_number=request.GET.get("re_num")
    inWork = TbinWork.objects.get(iw_number=iw_number)
    return render(request, 'wechat/inwork_change.html', {'inWork': inWork})


@csrf_exempt
def management_inWork_reset(request):
    if request.method == "POST":
        iw_number = request.POST.get('IW_number')
        iw_post = request.POST.get('IW_post')
        iw_depart = request.POST.get('IW_depart')
        w_time = request.POST.get('W_Time')
        w_place = request.POST.get('W_place')
        work = request.POST.get('Work')
        w_salary = request.POST.get('W_salary')
        w_reuire = request.POST.get('W_require')
        w_amount = request.POST.get('W_amount')
        ddl_time = request.POST.get('Ddl_time')
        inpub_time=timezone.now()
        w_ps = request.POST.get('W_ps')
        TbinWork.objects.filter(iw_number=iw_number).update(iw_post=iw_post, iw_depart=iw_depart, w_time=w_time, w_place=w_place, work=work,
                                       w_salary=w_salary, w_reuire=w_reuire, w_amount=w_amount, ddl_time=ddl_time, inpub_time=inpub_time, w_ps=w_ps)
        inwork_list = TbinWork.objects.all()
        return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})
    else:
        return HttpResponse("请求错误")

#校内兼职信息删除
@csrf_exempt
def management_inWork_delete(request):
    iw_number = request.GET.get('delete_num')
    TbinWork.objects.filter(iw_number=iw_number).delete()  #批量删除
    inwork_list = TbinWork.objects.all()
    return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})

