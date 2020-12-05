from django.shortcuts import HttpResponse,render
from django.utils import timezone
from django.template import loader
from .models import Tbcompany, Tbmanager, Tbstudent,Tbresume, Tbqualify, TbinWork, TboutWork, TbinResult, Tbapplication, TbinterviewApply, TbinterviewResult, TbinterviewNotice
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from threading import Timer
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
#校外兼职发布审核界面
@csrf_exempt
def work_examine(request):
    outwork_list = TboutWork.objects.filter(Q(ow_status="待审核") | Q(ow_status="已打回"))
    return render(request, 'wechat/work_examine.html', {'outwork_list': outwork_list})
#校外兼职信息发布界面
@csrf_exempt
def outwork_add(request):
    return render(request, 'wechat/outwork_add.html')

#校外
#面试申请总界面
def interview_list(request):
    interview_list = []
    list = TbinterviewApply.objects.all()
    for i in list:
        outwork = i.ow_number
        if outwork.ow_status=="面试申请中" or outwork.ow_status=="面试通知中" or outwork.ow_status=="面试阶段" or outwork.ow_status=="结果通知":
            dictionary = {}
            dictionary["ia_number"] = i.ia_number
            dictionary["ow_number"] = outwork.ow_number
            dictionary["ia_time"] = i.ia_time
            dictionary["ia_name"] = i.ia_name
            dictionary["phonenumber"] = i.phonenumber
            dictionary["a_time"] = i.a_time
            dictionary["apply_status"] = i.apply_status
            filterResult = TbinterviewNotice.objects.filter(ia_number=i.ia_number)
            if len(filterResult) > 0:
                application = TbinterviewNotice.objects.filter(ia_number=i.ia_number)
                dictionary["c_sure"] = application[0].c_sure
            else:
                dictionary["c_sure"] = "未开启"
            interview_list.append(dictionary)
    return render(request, 'wechat/interview_list.html', {'interview_list': interview_list})

#校外应聘学生查看
def stu_yingpin(request):
    ow_number = request.GET.get("yp_num")
    list = Tbapplication.objects.filter(ow_number=ow_number)
    outWork = TboutWork.objects.get(ow_number=ow_number)
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
        dictionary["school"] = student.school
        dictionary["major"] = student.major
        dictionary["pov_identity"] = student.pov_identity
        dictionary["e_mail"] = student.e_mail
        if inWork.In_status == "报名中" or inWork.In_status == "中止" or inWork.In_status == "报名结束":
            dictionary["s_sure"] = "未开启"
        else:
            application = Tbapplication.objects.filter(iw_number=iw_number).get(stu=stu_id)
            dictionary["s_sure"] = application.s_sure
        stu_yingpinlist.append(dictionary)
    return render(request, 'wechat/stu_yingpin.html', {'stu_yingpinlist': stu_yingpinlist})


#面试信息通知界面 HHL
def notice_send(request):
    return render(request, 'wechat/notice_send.html')

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