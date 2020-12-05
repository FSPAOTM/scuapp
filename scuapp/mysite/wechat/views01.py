from django.shortcuts import HttpResponse,render
from django.utils import timezone
from .models import Tbcompany, Tbmanager, Tbstudent,TbinWork, TboutWork, TbinResult, Tbapplication
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from threading import Timer

#报名结束状态生成（定时器自动更新）
def info_status():
    inlist = TbinWork.objects.filter(In_status='报名中')
    for i in inlist:
        iddl = (i.ddl_time - timezone.now()).days
        inow = Tbapplication.objects.filter(iw_number=i.iw_number).count()
        if iddl < 0 or inow >= int(i.w_amount):
            TbinWork.objects.filter(iw_number=i.iw_number).update(In_status='报名结束')
    outlist = TboutWork.objects.filter(ow_status="报名中")
    for j in outlist:
        oddl = (j.ddl_time - timezone.now()).days
        if oddl < 0:
            TboutWork.objects.filter(ow_number=j.ow_number).update(ow_status="报名结束")
    t = Timer(10, info_status, ())
    t.start()

info_status()

#后台管理界面

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
        if w_ddl <0:
            dictionary["w_out"] = "已截止"
            dictionary["w_ddl"] = "已截止"
        else:
            dictionary["w_out"] = w_out+"天"
            dictionary["w_ddl"] = w_ddl+"天"
        dictionary["w_now"]=w_now
        dictionary["iw_number"] = i.iw_number
        dictionary["iw_post"] = i.iw_post
        dictionary["work"] = i.work
        dictionary["w_amount"] = i.w_amount
        dictionary["w_reuire"] = i.w_reuire
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
        inwork_list = TbinWork.objects.filter(iw_post__contains=s_iw_post).filter(iw_number__contains=s_iw_number).filter(iw_depart__contains=s_iw_depart).filter(w_time__contains=s_w_time).filter(w_place__contains=s_w_place).filter(work__contains=s_work).filter(w_salary__contains=s_w_salary).filter(w_reuire__contains=s_w_reuire).filter(In_status__contains=s_In_status)
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
        s_ow_status = request.POST.get("s_ow_status")
        outwork_list = TboutWork.objects.filter(ow_post__contains=s_ow_post).filter(ow_number__contains=s_ow_number).filter(w_place_detail__contains=s_w_place_detail).filter(w_time__contains=s_w_time).filter(w_place__contains=s_w_place).filter(work__contains=s_work).filter(w_salary__contains=s_w_salary).filter(w_reuire__contains=s_w_reuire).filter(ow_status__contains=s_ow_status)#.filter(com_number__contains=company)
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
        if inWork.In_status== "报名中" or inWork.In_status == "中止" or inWork.In_status == "报名结束":
            dictionary["s_sure"] = "未开启"
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
        filterResult = TbinResult.objects.filter(iw_number=inwork)
        if len(filterResult) > 0:
            result_list = TbinResult.objects.get(iw_number=inwork)
            return render(request, 'wechat/inwork_result_change.html', {'result_list': result_list})
        else:
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
        inWork = TbinWork.objects.get(iw_number=iw_number)
        filterResult = TbinResult.objects.filter(iw_number=inWork)
        if len(filterResult) > 0:
            TbinResult.objects.filter(iw_number=inWork).update(inr_phonenum=inr_phonenum, r_time=r_time, result=result, r_ps=r_ps,
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
        TbinResult.objects.filter(iw_number=inWork).update(inr_phonenum=inr_phonenum, r_time=r_time, result=result, r_ps=r_ps,
                                      in_r_time=in_r_time)
        result_list = TbinResult.objects.get(iw_number=inWork)
        return render(request, 'wechat/inwork_result_change.html', {'result_list': result_list})
    else:
        return HttpResponse("请求错误")
#校外兼职通过
@csrf_exempt
def management_outWork_pass(request):
    ow_number = request.GET.get('pass_num')
    outWork = TboutWork.objects.get(ow_number=ow_number)
    if outWork.ow_status == "待审核":
        TboutWork.objects.filter(ow_number=ow_number).update(ow_status="报名中")
        outwork_list = TboutWork.objects.filter(Q(ow_status="待审核") | Q(ow_status="已打回"))
        return render(request, 'wechat/work_examine.html', {'outwork_list': outwork_list})
    else:
        return render(request, 'wechat/manage_error.html')
#校外兼职打回界面
@csrf_exempt
def management_outWork_reject(request):
    ow_number = request.GET.get('reject_num')
    outWork = TboutWork.objects.get(ow_number=ow_number)
    if outWork.ow_status == "待审核" or outWork.ow_status == "已打回" :
        c_phonenum = outWork.com_number.phone_num
        back_reason = outWork.back_reason
        return render(request, 'wechat/reject_result.html', {'ow_number': ow_number,'c_phonenum':c_phonenum,'back_reason': back_reason})
    else:
        return render(request, 'wechat/manage_error.html')
#校外兼职打回理由生成(保存按钮）
@csrf_exempt
def outWork_reject_result(request):
    if request.method == "POST":
        ow_number = request.POST.get('ow_number')
        back_reason = request.POST.get('back_reason')
        TboutWork.objects.filter(ow_number=ow_number).update(back_reason= back_reason)
        outWork = TboutWork.objects.get(ow_number=ow_number)
        c_phonenum = outWork.com_number.phone_num
        back_reason = outWork.back_reason
        return render(request, 'wechat/reject_result.html',
                      {'ow_number': ow_number, 'c_phonenum': c_phonenum, 'back_reason': back_reason})
    else:
        return HttpResponse("请求错误")
# 校外兼职打回理由生成(发送按钮）
@csrf_exempt
def outWork_reject_result_send(request):
    ow_number = request.GET.get('submit_num')
    outWork = TboutWork.objects.get(ow_number=ow_number)
    if outWork.back_reason != "None":
        TboutWork.objects.filter(ow_number=ow_number).update(ow_status="已打回")
        outwork_list = TboutWork.objects.filter(Q(ow_status="待审核") | Q(ow_status="已打回"))
        return render(request, 'wechat/work_examine.html', {'outwork_list': outwork_list})
    else:
        return render(request, 'wechat/manage_error.html')











