from django.shortcuts import HttpResponse,render
from django.utils import timezone
from django.template import loader
from .models import Tbcompany, Tbstudent,Tbresume, Tbqualify, TbinWork, TboutWork, TbinResult, Tbapplication, TbinterviewApply, TbinterviewResult, TbinterviewNotice
from django.db.models import Q
from threading import Timer
from django.http import JsonResponse
import json

#后台管理界面

#一大波界面导入
#首页
def index(request):
    return render(request, 'wechat/index.html')
#首页内框架页
def manage(request):
    return render(request, 'wechat/manage.html')
#登录界面
def login(request):
    return render(request, 'wechat/login.html')
#注册界面
def register(request):
    return render(request, 'wechat/register.html')
#忘记密码界面
def inwork_foregetpwd(request):
    return render(request, 'wechat/inwork_foregetpwd.html')
#校内兼职信息展示界面
def inwork_list(request):
    inwork_list = TbinWork.objects.all()
    return render(request, 'wechat/inwork_list.html', {'inwork_list': inwork_list})
#校内兼职信息发布界面
def inwork_add(request):
    return render(request, 'wechat/inwork_add.html')
#校外兼职信息展示界面
def outwork_list(request):
    outwork_list = TboutWork.objects.all()
    return render(request, 'wechat/outwork_list.html', {'outwork_list': outwork_list})
#校外兼职发布审核界面
def work_examine(request):
    outwork_list = TboutWork.objects.filter(Q(ow_status="待审核") | Q(ow_status="已打回"))
    return render(request, 'wechat/work_examine.html', {'outwork_list': outwork_list})
#校外兼职信息发布界面
def outwork_add(request):
    return render(request, 'wechat/outwork_add.html')
#校外
#面试申请总界面
def interview_list(request):
    interview_list = []
    list = TbinterviewApply.objects.all()
    for i in list:
        outwork = i.ow_number
        if outwork.ow_status=="面试申请中" or outwork.ow_status=="面试通知中" or outwork.ow_status=="面试阶段":
            dictionary = {}
            dictionary["ia_number"] = i.ia_number
            dictionary["ow_number"] = outwork.ow_number
            dictionary["ia_time"] = i.ia_time
            dictionary["ia_name"] = i.ia_name
            dictionary["phonenumber"] = i.phonenumber
            dictionary["a_time"] = i.a_time
            dictionary["apply_status"] = i.apply_status
            if outwork.ow_status != "面试申请中":
                interviewNotice = TbinterviewNotice.objects.get(ia_number=i.ia_number)
                dictionary["c_sure"] = interviewNotice.c_sure
            else:
                dictionary["c_sure"] = "未开启"
            interview_list.append(dictionary)
    return render(request, 'wechat/interview_list.html', {'interview_list': interview_list})

#校外应聘学生查看
def stu_yingpin(request):
    ia_number = request.GET.get("yp_num")
    interviewApply = TbinterviewApply.objects.get(ia_number=ia_number)
    outwork = interviewApply.ow_number
    list = Tbapplication.objects.filter(ow_number = outwork.ow_number)
    stu_yingpinlist = []
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
        dictionary["e_mail"] = student.e_mail
        dictionary["ap_reson"] = i.ap_reson
        dictionary["apply_status"] = i.apply_status
        if outwork.ow_status == "面试申请中":
            dictionary["s_sure"] = "未开启"
        else:
            interviewNotice = TbinterviewNotice.objects.get(ia_number=ia_number)
            list = interviewNotice.stu
            for i in list:
                if i == stu_id:
                    dictionary["s_sure"] = interviewNotice.s_sure[i]
        stu_yingpinlist.append(dictionary)
    return render(request, 'wechat/stu_yingpin.html', {'stu_yingpinlist': stu_yingpinlist})

#面试信息通知界面
def interview_notice_send(request):
    ia_number = request.GET.get("result_num")
    interviewApply = TbinterviewApply.objects.get(ia_number=ia_number)
    outwork = interviewApply.ow_number
    if outwork.ow_status == "面试申请中" or outwork.ow_status == "面试通知中":
        apply = Tbapplication.objects.filter(ow_number=outwork.ow_number).filter(apply_status="表筛已通过")
        filterResult = TbinterviewNotice.objects.filter(ia_number=ia_number)
        if len(filterResult) > 0:
            interviewNotice = TbinterviewNotice.objects.get(ia_number=ia_number)
            i_com = outwork.com_number.com_name
            i_num = str(apply.count())+"人"
            return render(request, 'wechat/notice_send.html', {'i_number': interviewNotice.i_number, 'ia_number': interviewNotice.ia_number, 'i_com': i_com,
                 'i_num': i_num, 'in_time': interviewNotice.in_time, 'i_address': interviewNotice.i_address})
        else:
            stu = []
            k = 0
            for i in apply:
                stu.append(i.stu.stu_id)
                k=k+1
            in_time=interviewApply.ia_time
            interviewNotice = TbinterviewNotice.objects.create(i_time=timezone.now(), ia_number=ia_number, stu=stu,in_time=in_time)
            interviewNotice.save()
            interviewNotice = TbinterviewNotice.objects.get(ia_number=ia_number)
            i_com = outwork.com_number.com_name
            i_num = str(k)+"人"
            return render(request, 'wechat/notice_send.html',{'i_number':interviewNotice.i_number,'ia_number':interviewNotice.ia_number,'i_com':i_com,'i_num':i_num,'in_time':interviewNotice.in_time,'i_address':interviewNotice.i_address})
    else:
        return render(request, 'wechat/manage_error.html')

#面试信息通知界面(保存按钮）
def interview_notice_send_save(request):
    ia_number = request.GET.get("result_num")
    interviewApply = TbinterviewApply.objects.get(ia_number=ia_number)
    outwork = interviewApply.ow_number
    if outwork.ow_status == "面试申请中" or outwork.ow_status == "面试通知中":
        apply = Tbapplication.objects.filter(ow_number=outwork.ow_number).filter(apply_status="表筛已通过")
        filterResult = TbinterviewNotice.objects.filter(ia_number=ia_number)
        if len(filterResult) > 0:
            interviewNotice = TbinterviewNotice.objects.get(ia_number=ia_number)
            i_com = outwork.com_number.com_name
            i_num = str(apply.count())+"人"
            return render(request, 'wechat/notice_send.html', {'i_number': interviewNotice.i_number, 'ia_number': interviewNotice.ia_number, 'i_com': i_com,
                 'i_num': i_num, 'in_time': interviewNotice.in_time, 'i_address': interviewNotice.i_address})
        else:
            stu = []
            k = 0
            for i in apply:
                stu.append(i.stu.stu_id)
                k=k+1
            in_time=interviewApply.ia_time
            interviewNotice = TbinterviewNotice.objects.create(i_time=timezone.now(), ia_number=ia_number, stu=stu,in_time=in_time)
            interviewNotice.save()
            interviewNotice = TbinterviewNotice.objects.get(ia_number=ia_number)
            i_com = outwork.com_number.com_name
            i_num = str(k)+"人"
            return render(request, 'wechat/notice_send.html',{'i_number':interviewNotice.i_number,'ia_number':interviewNotice.ia_number,'i_com':i_com,'i_num':i_num,'in_time':interviewNotice.in_time,'i_address':interviewNotice.i_address})


#面试信息打回 HHL
def back_reason(request):
    return render(request, 'wechat/back_reason.html')

#面试结果界面
def interview_result(request):
    interview_result = TbinterviewResult.objects.all()
    return render(request, 'wechat/interview_result.html', {'interview_result': interview_result})

#面试结果界面
def stu_result(request):
    return render(request, 'wechat/stu_result.html', {'stu_result': stu_result})

#企业列表界面
def company_list(request):
    company_list = Tbcompany.objects.all()
    return render(request, 'wechat/company_list.html', {'company_list': company_list})