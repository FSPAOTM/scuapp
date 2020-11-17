from django.shortcuts import HttpResponse,render
from django.utils import timezone
from django.template import loader
from .models import Tbcompany, Tbmanager, Tbstudent,Tbresume, Tbqualify,TbinWork,TboutWork, TbinResult,Tbapplication
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


#校外兼职信息展示界面
@csrf_exempt
def outwork_list(request):
    outwork_list = TboutWork.objects.all()
    return render(request, 'wechat/outwork_list.html', {'outwork_list': outwork_list})

#校外兼职信息发布界面
@csrf_exempt
def work_examine(request):
    return render(request, 'wechat/work_examine.html')

#校外兼职审核界面
@csrf_exempt
def outwork_add(request):
    return render(request, 'wechat/outwork_add.html')

#校内兼职报名处理界面
@csrf_exempt
def inworking_list(request):
    inworking_list = []
    list = TbinWork.objects.exclude(In_status ="已结束").exclude(In_status ="中止")
    for i in list:
        dictionary = {}
        w_now=Tbapplication.objects.filter(iw_number=i.iw_number).count()
        w_out=(timezone.now()-i.inpub_time).days
        w_ddl=(i.ddl_time-timezone.now()).days
        dictionary["w_now"]=w_now
        dictionary["iw_number"] = i.iw_number
        dictionary["iw_post"] = i.iw_post
        dictionary["work"] = i.work
        dictionary["w_amount"] = i.w_amount
        dictionary["w_reuire"] = i.w_reuire
        dictionary["w_out"] = w_out
        dictionary["w_ddl"] = w_ddl
        dictionary["In_status"] = i.In_status
        inworking_list.append(dictionary)
    return render(request, 'wechat/inworking_list.html', {'inworking_list': inworking_list})


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
    inWork=TbinWork.objects.get(iw_number=iw_number)
    if inWork.In_status == "报名中" or inWork.In_status == "报名结束" or inWork.In_status == "中止":
        TbinWork.objects.filter(iw_number=iw_number).update(In_status="中止")  #批量中止
        inwork_list = TbinWork.objects.all()
        return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})
    else:
        return render(request, 'wechat/manage_error.html')

#校内兼职启用
@csrf_exempt
def management_inWork_begin(request):
    iw_number = request.GET.get('begin_num')
    inWork = TbinWork.objects.get(iw_number=iw_number)
    if inWork.In_status == "报名中" or inWork.In_status == "报名结束" or inWork.In_status == "中止":
        TbinWork.objects.filter(iw_number=iw_number).update(In_status="报名中")  #批量启用
        inwork_list = TbinWork.objects.all()
        return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})
    else:
        return render(request, 'wechat/manage_error.html')

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
        s_In_status = request.POST.get("s_In_status")
        #s_ddl_time = request.POST.get("s_ddl_time")
        #s_inpub_time = request.POST.get("s_inpub_time")
        inwork_list = TbinWork.objects.filter(iw_post__contains=s_iw_post).filter(iw_number__contains=s_iw_number).filter(iw_depart__contains=s_iw_depart).filter(w_time__contains=s_w_time).filter(w_place__contains=s_w_place).filter(work__contains=s_work).filter(w_salary__contains=s_w_salary).filter(w_reuire__contains=s_w_reuire).filter(In_status__contains=s_In_status)
            #.filter(ddl_time__contains=s_ddl_time).filter(inpub_time__contains=s_inpub_time)
        return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})
    else:
        return HttpResponse("请求错误")

#校外兼职信息搜索
#存在问题：必须满足 %sab%的形式 中间有字检索不成功！！！！,时间无法检索！！应该为格式问题, com_number无法检索,因为是对象！！！
@csrf_exempt
def management_outwork_search(request):
    if request.method == "POST":
        s_ow_number = request.POST.get("s_ow_number")
        s_ow_post = request.POST.get("s_ow_post")
        s_w_time = request.POST.get("s_w_time")
        s_w_place_detail = request.POST.get("s_w_place_detail")
        s_w_place = request.POST.get("s_w_place")
        s_work = request.POST.get("s_work")
        s_w_salary = request.POST.get("s_w_salary")
        s_w_reuire = request.POST.get("s_w_reuire")
        #s_com_number = request.POST.get("s_com_number")
        s_ow_status = request.POST.get("s_ow_status")
        #s_ddl_time = request.POST.get("s_ddl_time")
        #s_ipub_time = request.POST.get("s_ipub_time")
        #company = TboutWork.objects.get(com_number=s_com_number)
        outwork_list = TboutWork.objects.filter(ow_post__contains=s_ow_post).filter(ow_number__contains=s_ow_number).filter(w_place_detail__contains=s_w_place_detail).filter(w_time__contains=s_w_time).filter(w_place__contains=s_w_place).filter(work__contains=s_work).filter(w_salary__contains=s_w_salary).filter(w_reuire__contains=s_w_reuire).filter(ow_status__contains=s_ow_status)#.filter(com_number__contains=company)
            #.filter(ddl_time__contains=s_ddl_time).filter(ipub_time__contains=s_ipub_time)
        return render(request, 'wechat/outwork_list.html', {'outwork_list': outwork_list})
    else:
        return HttpResponse("请求错误")

#校外兼职信息删除
@csrf_exempt
def management_outWork_delete(request):
    ow_number = request.GET.get('delete_num')
    TboutWork.objects.filter(ow_number=ow_number).delete()  #批量删除
    outwork_list = TboutWork.objects.all()
    return render(request, 'wechat/outwork_list.html', {'outwork_list': outwork_list})

#校外兼职中止
@csrf_exempt
def management_outWork_stop(request):
    ow_number = request.GET.get('stop_num')
    outWork = TboutWork.objects.get(ow_number=ow_number)
    if outWork.ow_status == "报名中" or outWork.ow_status == "待审核" or outWork.ow_status == "中止":
        TboutWork.objects.filter(ow_number=ow_number).update(ow_status="中止")  #批量中止
        outwork_list = TboutWork.objects.all()
        return render(request, 'wechat/outwork_list.html', {'outwork_list': outwork_list})
    else:
        return render(request, 'wechat/manage_error.html')

#校外兼职启用
@csrf_exempt
def management_outWork_begin(request):
    ow_number = request.GET.get('begin_num')
    outWork = TboutWork.objects.get(ow_number=ow_number)
    if outWork.ow_status == "报名中" or outWork.ow_status == "待审核" or outWork.ow_status == "中止":
        TboutWork.objects.filter(ow_number=ow_number).update(ow_status="待审核")  #批量启用
        outwork_list = TboutWork.objects.all()
        return render(request, 'wechat/outwork_list.html', {'outwork_list': outwork_list})
    else:
        return render(request, 'wechat/manage_error.html')

#校外兼职通过
@csrf_exempt
def management_outWork_pass(request):
    ow_number = request.GET.get('pass_num')
    outWork = TboutWork.objects.get(ow_number=ow_number)
    if outWork.ow_status == "待审核":
        TboutWork.objects.filter(ow_number=ow_number).update(ow_status="审核通过")  #批量中止
        outwork_list = TboutWork.objects.all()
        return render(request, 'wechat/work_examine.html', {'outwork_list': outwork_list})
    else:
        return render(request, 'wechat/manage_error.html')

#校外兼职打回
@csrf_exempt
def outWork_reject_result(request):
    if request.method == "POST":
        ow_number = request.POST.get('ow_number')
        inr_phonenum = request.POST.get('inr_phonenum')
        result = request.POST.get('result')
        reject = request.POST.get('reject')
#        in_r_time = timezone.now()
#        filterResult = TbinResult.objects.filter(ow_number=ow_number)
#        inWork = TbinWork.objects.get(iw_number=iw_number)
#        if len(filterResult) > 0:
#            TbinResult.objects.filter(iw_number=iw_number).update(inr_phonenum=inr_phonenum, r_time=r_time,
#                                                                  result=result, r_ps=r_ps,
#                                                                  in_r_time=in_r_time)
#        else:
#            inworking = TbinResult.objects.create(inr_phonenum=inr_phonenum, r_time=r_time, result=result, r_ps=r_ps,
#                                                  in_r_time=in_r_time, iw_number=inWork)
#            inworking.save()
#        result_list = TbinResult.objects.get(iw_number=inWork)
#        return render(request, 'wechat/inwork_result_change.html', {'result_list': result_list})
#    else:
#        return HttpResponse("请求错误")


#校外兼职信息修改
@csrf_exempt
def management_outWork_reset_show(request):
    ow_number=request.GET.get("re_num")
    outWork = TboutWork.objects.get(ow_number=ow_number)
    return render(request, 'wechat/outWork_change.html', {'outWork': outWork})


@csrf_exempt
def management_outWork_reset(request):
    if request.method == "POST":
        ow_number = request.POST.get('ow_number')
        ow_post = request.POST.get('ow_post')
        w_place_detail = request.POST.get('w_place_detail')
        w_time = request.POST.get('W_Time')
        w_place = request.POST.get('W_place')
        work = request.POST.get('Work')
        w_salary = request.POST.get('W_salary')
        w_reuire = request.POST.get('W_require')
        w_amount = request.POST.get('W_amount')
        ddl_time = request.POST.get('Ddl_time')
        ipub_time=timezone.now()
        w_ps = request.POST.get('W_ps')
        TboutWork.objects.filter(ow_number=ow_number).update(ow_post=ow_post, w_place_detail=w_place_detail, w_time=w_time, w_place=w_place, work=work,
                                       w_salary=w_salary, w_reuire=w_reuire, w_amount=w_amount, ddl_time=ddl_time, ipub_time=ipub_time, w_ps=w_ps)
        outwork_list = TboutWork.objects.all()
        return render(request, 'wechat/outwork_list.html', {'outwork_list': outwork_list})
    else:
        return HttpResponse("请求错误")

#校外兼职信息发布
@csrf_exempt
def management_outWork_release(request):
    if request.method == "POST":
        ow_post = request.POST.get('ow_post')
        w_place_detail = request.POST.get('w_place_detail')
        w_time = request.POST.get('W_Time')
        w_place = request.POST.get('W_place')
        work = request.POST.get('Work')
        w_salary = request.POST.get('W_salary')
        w_reuire = request.POST.get('W_require')
        w_amount = request.POST.get('W_amount')
        ddl_time = request.POST.get('Ddl_time')
        ipub_time = timezone.now()
        com_number = request.POST.get('com_number')
        company = Tbcompany.objects.get(com_number=com_number)
        w_ps = request.POST.get('W_ps')
        outWork=TboutWork.objects.create(ow_post=ow_post, w_place_detail=w_place_detail, w_time=w_time, w_place=w_place, work=work,
                                       w_salary=w_salary, w_reuire=w_reuire, w_amount=w_amount, ddl_time=ddl_time, ipub_time=ipub_time, w_ps=w_ps, com_number=company)
        outWork.save()
        outWork_list = TboutWork.objects.all()
        return render(request, 'wechat/outWork_list.html', {'outWork_list': outWork_list})
    else:
        return HttpResponse("请求错误")

###################################################信息处理部分的视图！！（待修改）

#校内兼职报名学生简历
@csrf_exempt
def inwork_stu_ifo(request):
    iw_number = request.GET.get("stu_ifo_num")
    list=Tbapplication.objects.filter(iw_number=iw_number)
    inWork = TbinWork.objects.get(iw_number=iw_number)
    inwork_stu_list = []
    for i in list:
        stu_id = i.stu.stu_id
        student = Tbstudent.objects.get(stu_id=stu_id)
        dictionary = {}
        dictionary["stu_id"] = stu_id
        dictionary["name"] = student.name
        dictionary["age"] = student.age
        dictionary["sex"] = student.sex
        dictionary["phonenumber"] = student.phonenumber_phonenumberphonenumber_phonenumber
        dictionary["grade"] = student.grade
        dictionary["school"] = student.school
        dictionary["major"] = student.major
        dictionary["pov_identity"] = student.pov_identity
        dictionary["e_mail"] = student.e_mail
        if inWork.In_status== "报名中" or inWork.In_status == "中止":
            dictionary["s_sure"] = "未通知"
        else:
            application= Tbapplication.objects.filter(iw_number=iw_number).get(stu=stu_id)
            dictionary["s_sure"] = application.s_sure
        inwork_stu_list.append(dictionary)
    return render(request, 'wechat/inwork_stu_ifo.html', {'inwork_stu_list': inwork_stu_list})


#校内兼职结果搜索
@csrf_exempt
def management_inworking_search(request):
    if request.method == "POST":
        s_iw_number = request.POST.get("s_iw_number")
        s_iw_post = request.POST.get("s_iw_post")
        s_work = request.POST.get("s_work")
        s_w_reuire = request.POST.get("s_w_reuire")
        #s_w_out = request.POST.get("s_w_out")
        #s_w_ddl = request.POST.get("s_w_ddl")
        s_w_status = request.POST.get("s_w_status")
        list = TbinWork.objects.filter(iw_post__contains=s_iw_post).filter(iw_number__contains=s_iw_number).filter(work__contains=s_work).filter(w_reuire__contains=s_w_reuire).filter(In_status__contains=s_w_status).exclude(In_status="已结束").exclude(In_status="中止")
        inworking_list = []
        for i in list:
            dictionary = {}
            w_now = Tbapplication.objects.filter(iw_number=i.iw_number).count()
            w_out = (timezone.now() - i.inpub_time).days
            w_ddl = (i.ddl_time - timezone.now()).days
            dictionary["w_now"] = w_now
            dictionary["iw_number"] = i.iw_number
            dictionary["iw_post"] = i.iw_post
            dictionary["work"] = i.work
            dictionary["w_amount"] = i.w_amount
            dictionary["w_reuire"] = i.w_reuire
            dictionary["w_out"] = w_out
            dictionary["w_ddl"] = w_ddl
            dictionary["In_status"] = i.In_status
            inworking_list.append(dictionary)
        return render(request, 'wechat/inworking_list.html', {'inworking_list': inworking_list})
    else:
        return HttpResponse("请求错误")

#招聘结果发送
@csrf_exempt
def inwork_result(request):
    iw_number = request.GET.get("result_num")
    inwork = TbinWork.objects.get(iw_number=iw_number)

    if inwork.In_status == "报名结束" or inwork.In_status == "结果通知中":
        return render(request, 'wechat/inwork_result.html', {'iw_number': iw_number})
    else:
        return render(request, 'wechat/manage_error.html')

#应该多表和学生相连(保存按钮）
@csrf_exempt
def management_inWork_result(request):
    if request.method == "POST":
        iw_number = request.POST.get('iw_number')
        inr_phonenum = request.POST.get('inr_phonenum')
        r_time = request.POST.get('r_time')
        result = request.POST.get('result')
        r_ps = request.POST.get('r_ps')
        in_r_time = timezone.now()
        filterResult = TbinResult.objects.filter(iw_number=iw_number)
        inWork = TbinWork.objects.get(iw_number=iw_number)
        if len(filterResult) > 0:
            TbinResult.objects.filter(iw_number=iw_number).update(inr_phonenum=inr_phonenum, r_time=r_time, result=result, r_ps=r_ps,
                                      in_r_time=in_r_time)
        else:
            inworking = TbinResult.objects.create(inr_phonenum=inr_phonenum, r_time=r_time, result=result, r_ps=r_ps,
                                                  in_r_time=in_r_time,iw_number= inWork)
            inworking.save()
        result_list = TbinResult.objects.get(iw_number=inWork)
        return render(request, 'wechat/inwork_result_change.html', {'result_list': result_list})
    else:
        return HttpResponse("请求错误")

#提交按钮
@csrf_exempt
def inwork_result_submit(request):
    iw_number = request.GET.get("submit_num")
    filterResult = TbinResult.objects.filter(iw_number=iw_number)
    if len(filterResult) > 0:
        TbinWork.objects.filter(iw_number=iw_number).update(In_status = "结果通知中")
        inworking_list = []
        list = TbinWork.objects.exclude(In_status="已结束").exclude(In_status="中止")
        for i in list:
            dictionary = {}
            w_now = Tbapplication.objects.filter(iw_number=i.iw_number).count()
            w_out = (timezone.now() - i.inpub_time).days
            w_ddl = (i.ddl_time - timezone.now()).days
            dictionary["w_now"] = w_now
            dictionary["iw_number"] = i.iw_number
            dictionary["iw_post"] = i.iw_post
            dictionary["work"] = i.work
            dictionary["w_amount"] = i.w_amount
            dictionary["w_reuire"] = i.w_reuire
            dictionary["w_out"] = w_out
            dictionary["w_ddl"] = w_ddl
            dictionary["In_status"] = i.In_status
            inworking_list.append(dictionary)
        return render(request, 'wechat/inworking_list.html', {'inworking_list': inworking_list})
    else:
        return render(request, 'wechat/manage_error.html')

#修改校内招聘结果通知
@csrf_exempt
def management_inWork_result_change(request):
    if request.method == "POST":
        iw_number = request.POST.get('iw_number')
        inr_phonenum = request.POST.get('inr_phonenum')
        r_time = request.POST.get('r_time')
        result = request.POST.get('result')
        r_ps = request.POST.get('r_ps')
        in_r_time = timezone.now()
        inWork = TbinWork.objects.get(iw_number=iw_number)
        TbinResult.objects.filter(iw_number=iw_number).update(inr_phonenum=inr_phonenum, r_time=r_time, result=result, r_ps=r_ps,
                                      in_r_time=in_r_time)
        result_list = TbinResult.objects.get(iw_number=iw_number)
        return render(request, 'wechat/inwork_result_change.html', {'result_list': result_list})
    else:
        return HttpResponse("请求错误")



