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

#学生工作经历详情界面
def stu_experience(request):
    stu_id = request.GET.get('stu_num')
    stu = Tbstudent.objects.get(stu_id=stu_id)
    list = Tbapplication.objects.filter(stu=stu)
    stu_inwork=[]
    stu_outwork=[]
    for i in list:
        if i.ow_number is None:
            dictionary = {}
            dictionary["iw_number"] = i.iw_number.iw_number
            dictionary["iw_post"] = i.iw_number.iw_post
            dictionary["iw_depart"] = i.iw_number.iw_depart
            dictionary["work"] = i.iw_number.work
            dictionary["apply_status"] = i.apply_status
            dictionary["In_status"] = i.iw_number.In_status
            inResult = TbinResult.objects.filter(iw_number=i.iw_number)
            if len(inResult) > 0:
                inResult1 = TbinResult.objects.get(iw_number=i.iw_number)
                dictionary["begin_time"] = inResult1.r_time
                feedbackEr0 = TbfeedbackEr.objects.filter(stu=stu).filter(iw_number=i.iw_number).filter(
                    fb_direction="学生评价企业")
                if len(feedbackEr0) > 0:
                    feedbackEr1 = TbfeedbackEr.objects.filter(stu=stu).filter(iw_number=i.iw_number).get(
                        fb_direction="学生评价企业")
                    dictionary["end_time"] = str(feedbackEr1.fb_time)
                else:
                    dictionary["end_time"] = "未结束"
            else:
                dictionary["begin_time"] = "未入职"
                dictionary["end_time"] = "未入职"
            stu_inwork.append(dictionary)
        else:
            dictionary1 = {}
            dictionary1["ow_number"] = i.ow_number.ow_number
            dictionary1["ow_post"] = i.ow_number.ow_post
            dictionary1["com_name"] = i.ow_number.com_number.com_name
            dictionary1["work"] = i.ow_number.work
            dictionary1["apply_status"] = i.apply_status
            dictionary1["ow_status"] = i.ow_number.ow_status
            dictionary1["reason"] = i.ap_reson
            interviewApply = TbinterviewApply.objects.filter(ow_number=i.ow_number)
            if len(interviewApply)>0:
                interviewApply = TbinterviewApply.objects.get(ow_number=i.ow_number)
                interviewNotice = TbinterviewNotice.objects.filter(ia_number=interviewApply.ia_number)
                if len(interviewNotice)>0:
                    interviewNotice = TbinterviewNotice.objects.get(ia_number=interviewApply.ia_number)
                    interviewResult = TbinterviewResult.objects.filter(i_number=interviewNotice)
                    if len(interviewResult)>0:
                        interviewResult = TbinterviewResult.objects.get(i_number=interviewNotice)
                        dictionary1["begin_time"]=interviewResult.ir_rtime
                        feedbackEr0 = TbfeedbackEr.objects.filter(stu=stu).filter(ow_number=i.ow_number).filter(
                            fb_direction="学生评价企业")
                        if len(feedbackEr0) > 0:
                            feedbackEr1 = TbfeedbackEr.objects.filter(stu=stu).filter(ow_number=i.ow_number).get(
                                fb_direction="学生评价企业")
                            dictionary1["end_time"] = str(feedbackEr1.fb_time)
                        else:
                            dictionary1["end_time"] = "未结束"
                    else:
                        dictionary1["begin_time"] = "未入职"
                        dictionary1["end_time"] = "未入职"
                else:
                    dictionary1["begin_time"] = "未入职"
                    dictionary1["end_time"] = "未入职"
            else:
                dictionary1["begin_time"] = "未入职"
                dictionary1["end_time"] = "未入职"
            stu_outwork.append(dictionary1)
    return render(request, 'wechat/stu_work.html', {'stu_inwork': stu_inwork, 'stu_outwork': stu_outwork})


#学生简历查看界面（界面 emmm)
def stu_manage_resume_list(request):
    str = request.GET.get('res_num')
    res_id =str[17:27]
    resume = Tbresume.objects.get(res_id=res_id)
    return render(request, 'wechat/stu_resume.html',{'resume': resume})

#企业管理
#企业列表界面
def company_manage_list(request):
    company = Tbcompany.objects.all()
    company_list=[]
    for i in company:
        dictionary = {}
        dictionary["com_number"] = i.com_number
        dictionary["com_name"] = i.com_name
        dictionary["phone_num"] = i.phone_num
        dictionary["com_leader"] = i.com_leader
        dictionary["com_address"] = i.com_address
        dictionary["e_mail"] = i.e_mail
        dictionary["com_License"] = i.com_License.com_license
        dictionary["com_condition"] = i.com_license.com_condition
        dictionary["com_business"] = i.com_license.com_business
        company_list.append(dictionary)
    return render(request, 'wechat/company_list.html', {'company_list': company_list})

#企业所发布兼职列表
def company_work(request):
    com_num = request.GET.get('com_num')
    company = Tbcompany.objects.get(com_number = com_num)
    outwork = TboutWork.objects.filter(com_number = company)
    company_work = []
    for i in outwork:
        dictionary = {}
        dictionary["ow_number"] = i.ow_number
        dictionary["ow_post"] = i.ow_post
        dictionary["w_time"] = i.w_time
        dictionary["w_place"] = i.w_place
        dictionary["work"] = i.work
        dictionary["ipub_time"] = str(i.ipub_time)
        dictionary["ow_status"] = i.ow_status
        company_work.append(dictionary)
    return render(request, 'wechat/company_work.html', {'company_work': company_work})

#企业兼职录取与招聘情况
def company_employed(request):
    ow_number = request.GET.get('ow_number')
    company = Tbcompany.objects.get(com_number = com_num)
    outwork = TboutWork.objects.filter(com_number = company)
    company_work = []
    for i in outwork:
        dictionary = {}
        dictionary["ow_number"] = i.ow_number
        dictionary["ow_post"] = i.ow_post
        dictionary["w_time"] = i.w_time
        dictionary["w_place"] = i.w_place
        dictionary["work"] = i.work
        dictionary["ipub_time"] = str(i.ipub_time)
        dictionary["ow_status"] = i.ow_status
        company_work.append(dictionary)
    return render(request, 'wechat/company_work.html', {'company_work': company_work})

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





