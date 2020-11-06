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
#注册界面
@csrf_exempt
def register(request):
    return render(request, 'wechat/register.html')

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
@csrf_exempt
def management_login(request):
    if request.method == "POST":
        manager_id = request.POST.get("manager_id")
        password = request.POST.get("password")
        try:
            user = Tbmanager.objects.get(manager_id=manager_id)
            if user.password != password:
                error_msg = "用户名或密码错误"
                return render(request, 'wechat/login.html', {'error_msg': error_msg})
        except Tbmanager.DoesNotExist as e:
            error_msg = "用户名不存在"
            return render(request, 'wechat/login.html', {'error_msg': error_msg})
        # 登录成功
        return render(request, 'wechat/index.html')
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

#校内兼职信息搜索
def management_inwork_search(request):
    s_iw_number = request.GET.get("s_iw_number")
    s_iw_post = request.GET.get("s_iw_post")
    s_iw_depart = request.GET.get("s_iw_depart")
    s_w_time = request.GET.get("s_w_time")
    s_w_place = request.GET.get("s_w_place")
    s_work = request.GET.get("s_work")
    s_w_salary = request.GET.get("s_w_salary")
    s_w_reuire = request.GET.get("s_w_reuire")
    s_ddl_time = request.GET.get("s_ddl_time")
    s_inpub_time = request.GET.get("s_inpub_time")
    inwork_search = TbinWork.objects.filter(iw_post__contains=s_iw_post, iw_depart__contains=s_iw_depart, w_time__contains=s_w_time, w_place__contains=s_w_place,
                            work__contains=s_work, w_salary__contains=s_w_salary, w_reuire__contains=s_w_salary )
    return render(request, 'wechat/inwork_search.html', {'inwork_search': inwork_search})


#注册管理者
def management_inwork_register(request):
    if request.method == "POST":
        manager_id = request.POST.get("manager_id")
        name = request.POST.get("name")
        phonenumber = request.POST.get("phonenumber")
        password = request.POST.get("password")
        school = request.POST.get("school")
        sex = request.POST.get("sex")
        e_mail =request.POST.get("e_mail")





