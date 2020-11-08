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
#首页内框架页
@csrf_exempt
def manage(request):
    return render(request, 'wechat/manage.html')
#登录界面
@csrf_exempt
def login(request):
    return render(request, 'wechat/login.html')
#注册界面
@csrf_exempt
def register(request):
    return render(request, 'wechat/register.html')
#忘记密码界面
@csrf_exempt
def inwork_foregetpwd(request):
    return render(request, 'wechat/inwork_foregetpwd.html')

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
#登录管理者
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

#注册管理者
@csrf_exempt
def management_inwork_register(request):
    if request.method == "POST":
        manager_id = request.POST.get("manager_id")
        name = request.POST.get("name")
        phonenumber = request.POST.get("phonenumber")
        password = request.POST.get("password")
        filterResult = Tbmanager.objects.filter(manager_id=manager_id)
        if len(filterResult) > 0:
            error_msg = "用户已存在"
            return render(request, 'wechat/register.html', {'error_msg': error_msg})
        else:
            user = Tbmanager.objects.create(manager_id=manager_id, name=name, phonenumber=phonenumber,
                                            password=password)
            user.save()
            return render(request, 'wechat/register_success.html')
        #注册成功的显示？？？（界面？？）
    else:
        return HttpResponse("请求错误")

#忘记密码
@csrf_exempt
def management_forgetpwd(request):
    if request.method == "POST":
        manager_id = request.POST.get("manager_id")
        phonenumber = request.POST.get("phonenumber")
        password = request.POST.get("password")
        filterResult = Tbmanager.objects.filter(manager_id=manager_id)
        manage = Tbmanager.objects.get(manager_id=manager_id)
        if len(filterResult) > 0:
            if manage.phonenumber != phonenumber:
                error_msg = "手机号错误"
                return render(request, 'wechat/inwork_foregetpwd.html', {'error_msg': error_msg})
            else:
                Tbmanager.objects.filter(manager_id=manager_id).update(password=password)
                return render(request, 'wechat/xiugai_success.html')
            #修改成功显示？？？（界面？？）
        else:
            error_msg = "用户不存在"
            return render(request, 'wechat/inwork_foregetpwd.html', {'error_msg': error_msg})
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

#校内兼职中止
@csrf_exempt
def management_inWork_stop(request):
    iw_number = request.GET.get('stop_num')
    TbinWork.objects.filter(iw_number=iw_number).update(In_status="中止")  #批量中止
    inwork_list = TbinWork.objects.all()
    return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})

#校内兼职启用
@csrf_exempt
def management_inWork_begin(request):
    iw_number = request.GET.get('begin_num')
    TbinWork.objects.filter(iw_number=iw_number).update(In_status="报名中")  #批量启用
    inwork_list = TbinWork.objects.all()
    return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})

#校内兼职信息搜索
#存在问题：必须满足 %sab%的形式 中间有字检索不成功！！！！,时间无法检索！！应该为格式问题
@csrf_exempt
def management_inwork_search(request):
    if request.method == "POST":
        s_iw_number = request.POST.get("s_iw_number")
        s_iw_post = request.POST.get("s_iw_post")
        s_iw_depart = request.POST.get("s_iw_depart")
        s_w_time = request.POST.get("s_w_time")
        s_w_place = request.POST.get("s_w_place")
        s_work = request.POST.get("s_work")
        s_w_salary = request.POST.get("s_w_salary")
        s_w_reuire = request.POST.get("s_w_reuire")
        #s_ddl_time = request.POST.get("s_ddl_time")
        #s_inpub_time = request.POST.get("s_inpub_time")
        inwork_list = TbinWork.objects.filter(iw_post__contains=s_iw_post).filter(iw_number__contains=s_iw_number).filter(iw_depart__contains=s_iw_depart).filter(w_time__contains=s_w_time).filter(w_place__contains=s_w_place).filter(work__contains=s_work).filter(w_salary__contains=s_w_salary).filter(w_reuire__contains=s_w_reuire)
            #.filter(ddl_time__contains=s_ddl_time).filter(inpub_time__contains=s_inpub_time)
        return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})
    else:
        return HttpResponse("请求错误")









