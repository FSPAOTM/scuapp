from django.shortcuts import HttpResponse,render
from django.utils import timezone
from .models import Tbcompany, Tbstudent,Tbresume, Tbqualify, TbinWork, TboutWork, TbinResult, Tbapplication, TbinterviewApply, TbinterviewResult, TbinterviewNotice, TbfeedbackEr, TbfeedbackStu
from django.db.models import Q
from threading import Timer
from django.http import JsonResponse
from . import views01
import json

#后台管理界面

#用户管理

#学生管理
#学生列表界面
def stu_manage_list(request):
    stu_list = Tbstudent.objects.all()
    return render(request, 'wechat/stu_list.html', {'stu_list': stu_list})

#学生简历查看界面 修改中... 未添加URL
def stu_manage_resume_list(request):
    return render(request, 'wechat/stu_resume.html')



#企业管理
#企业列表界面——HHL
def company_manage_list(request):
    company_list = Tbcompany.objects.all()
    return render(request, 'wechat/company_list.html', {'company_list': company_list})

#评价管理
#校外兼职评价展示界面——HHL 12/11
def outwork_feedback(request):
    out_feed = ["balabala"]
    feed_content = ["bilibili"]
    return render(request, 'wechat/outwork_feedback.html')

#校内兼职评价展示界面——HHL 12/11
def inwork_feedback(request):
    in_feed = ["jijiwaiwai"]
    feed_content = ["jijizhazha"]
    return render(request, 'wechat/inwork_feedback.html')

#学生评价展示界面——HHL 12/13
def stu_feedback_show(request):
    stu_feed = ["哇哇哇"]
    feed_content = ["awsl"]
    return render(request, 'wechat/stu_feedback_show.html')



