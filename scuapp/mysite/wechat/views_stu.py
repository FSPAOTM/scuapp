from django.shortcuts import HttpResponse,render
from django.template import loader
from .models import Tbcompany, Tbmanager, Tbstudent,Tbresume, Tbqualify,TbinWork,TboutWork,Tbapplication,TbinterviewNotice,TbfeedbackEr,TbinterviewApply
from django.http import JsonResponse
from django.utils import timezone
import json
from itertools import chain
from . import views01
#小程序界面

#smianshitongzhi 学生面试通知显示
def Stu_interview_notice_show(request):
    stu_id = request.GET.get('user')
    student = Tbstudent.objects.get(stu_id=stu_id)
    application = Tbapplication.objects.filter(stu=student).filter(apply_status="面试中")
    plays = []
    for i in application:
        interviewApply = TbinterviewApply.objects.get(ow_number=i.ow_number)
        interviewNotice = TbinterviewNotice.objects.get(ia_number=interviewApply.ia_number)
        stu = interviewNotice.stu.replace("'", '"')
        stu = json.loads(stu)
        sure = interviewNotice.s_sure.replace("'", '"')
        sure = json.loads(sure)
        k = 0
        for j in stu:
            if j == stu_id:
                s_sure = sure[k]
            k = k + 1
        if s_sure == "未确认":
            plays.append({'ow_number': i.ow_number.ow_number, 'post': i.ow_number.ow_post, 'time': interviewNotice.in_time,
                          'place': interviewNotice.i_address})
    plays_json = json.dumps(plays, ensure_ascii=False)
    return HttpResponse(plays_json)

#smianshitongzhi 学生面试通知确认
def Stu_interview_notice_sure(request):
    if request.method == "POST":
        stu_id = request.POST.get('user')
        number = request.POST.get('ow_number')
        ow_number = TboutWork.objects.get(ow_number=number)
        interviewApply = TbinterviewApply.objects.get(ow_number=ow_number)
        interviewNotice = TbinterviewNotice.objects.get(ia_number=interviewApply.ia_number)
        Notice = TbinterviewNotice.objects.filter(ia_number=interviewApply.ia_number)
        stu = interviewNotice.stu.replace("'", '"')
        stu = json.loads(stu)
        sure = interviewNotice.s_sure.replace("'", '"')
        sure = json.loads(sure)
        k = 0
        for j in stu:
            if j == stu_id:
                sure[k] = "已确认"
            k = k + 1
        Notice.update(s_sure=sure)
        views01.interview_sure(Notice[0].i_number)
        return HttpResponse("确认成功")
    else:
        return HttpResponse("请求错误")



#sfeedback 未调试
def feedbackEr(request):
    if request.method == "POST":
        stu = request.POST.get('stuNumber')
        ow_number = request.POST.get('ow_number')
        iw_number = request.POST.get('iw_number')
        score = request.POST.get('score')
        trust = request.POST.get('trust')
        timely = request.POST.get('timely')
        flexible = request.POST.get('flexible')
        salary = request.POST.get('salary')
        meaning = request.POST.get('meaning')
        more = request.POST.get('more')
        fb_content = []
        fb_content.append(score)
        fb_content.append(trust)
        fb_content.append(timely)
        fb_content.append(flexible)
        fb_content.append(salary)
        fb_content.append(meaning)
        fb_content.append(more)
        stu = Tbstudent.objects.get(stu_id=stu)
        if iw_number != '':
            iw_number = TbinWork.objects.get(iw_number=iw_number)
            result = TbfeedbackEr.objects.create(fb_content=fb_content, fb_direction='学生评价企业',fb_time=timezone.now(), iw_number=iw_number,stu=stu)
            Tbapplication.objects.filter(stu=stu,iw_number=iw_number).update(apply_status='已评价')

        else:
            ow_number = TboutWork.objects.get(ow_number=ow_number)
            result = TbfeedbackEr.objects.create(fb_content=fb_content, fb_direction='学生评价企业',fb_time=timezone.now(), ow_number=ow_number,stu=stu)
            Tbapplication.objects.filter(stu=stu,ow_number=ow_number).update(apply_status='已评价')
        result.save()
        return HttpResponse("评价成功")
    else:
        return HttpResponse("请求错误")

#学生面试结果确认 注意 传工作编号 校内校外编号都传？是否区分校内外？？