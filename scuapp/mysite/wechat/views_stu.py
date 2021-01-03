from django.shortcuts import HttpResponse
from .models import Tbstudent,TbinWork,TboutWork,Tbapplication,TbinterviewNotice,TbfeedbackEr,TbinterviewApply,TbinResult,TbinterviewResult,Tbcompany
from django.utils import timezone
import json
from django.db.models import Q
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

#smianshixinxi 学生面试信息显示
def Stu_interview_information_show(request):
    stu_id = request.GET.get('stu_number')
    number = request.GET.get('ow_number')
    ow_number = TboutWork.objects.get(ow_number=number)
    interviewApply = TbinterviewApply.objects.get(ow_number=ow_number)
    interviewNotice = TbinterviewNotice.objects.get(ia_number=interviewApply.ia_number)
    stu = interviewNotice.stu.replace("'", '"')
    stu = json.loads(stu)
    sure = interviewNotice.s_sure.replace("'", '"')
    sure = json.loads(sure)
    plays = []
    k = 0
    for j in stu:
        if j == stu_id:
            if sure[k] == "已确认":
                plays.append(
                    {'ow_number': number, 'post': ow_number.ow_post, 'time': interviewNotice.in_time,
                     'place': interviewNotice.i_address})
            k = k + 1
    plays_json = json.dumps(plays, ensure_ascii=False)
    return HttpResponse(plays_json)

#sjieguotongzhi 学生结果通知显示
def Stu_result_show(request):
    stu_id = request.GET.get('stu_id')
    student = Tbstudent.objects.get(stu_id=stu_id)
    application1 = Tbapplication.objects.filter(stu=student).filter(apply_status="已录用").filter(s_sure="未确认")
    plays = []
    for i in application1:
        if i.iw_number is not None:
            inResult = TbinResult.objects.get(iw_number =i.iw_number)
            result = "您已被录用，请在" + inResult.r_time +"前联系负责人并按时报到"
            plays.append({'type':"校内兼职",'iw_number': i.iw_number.iw_number, 'post': i.iw_number.iw_post, 'result': result,
                          'phonenum': inResult.inr_phonenum,'ps': inResult.r_ps,'success':True,'fail':False})
        else:
            interviewApply = TbinterviewApply.objects.get(ow_number =i.ow_number)
            interviewNotice = TbinterviewNotice.objects.get(ia_number=interviewApply.ia_number)
            interviewResult = TbinterviewResult.objects.get(i_number =interviewNotice)
            address = i.ow_number.w_place + i.ow_number.w_place_detail
            plays.append({'type': "校外兼职", 'ow_number': i.ow_number.ow_number, 'post': i.ow_number.ow_post,
                          'result': "您已被录用，请按时报到",
                          'time': interviewResult.ir_rtime, 'address': address, 'ps': interviewResult.ir_ps,'success':True,'fail':False})
    application2 = Tbapplication.objects.filter(stu=student).filter(Q(apply_status="未录用") | Q(apply_status="表筛未通过")).filter(s_sure="未确认")
    for j in application2:
        plays.append({'type': "校外兼职", 'ow_number': j.ow_number.ow_number, 'post': j.ow_number.ow_post,
                          'result': "很遗憾，您未被录用，请继续加油！",'success':False,'fail':True})
    plays_json = json.dumps(plays, ensure_ascii=False)
    return HttpResponse(plays_json)

#sluyongxinxi 学生录用信息显示
def Stu_result_information_show(request):
    ow_number = request.GET.get('ow_number')
    iw_number = request.GET.get('iw_number')
    stu_id = request.GET.get('stu_number')
    student = Tbstudent.objects.get(stu_id=stu_id)
    plays = []
    if iw_number =="null":
        ow_number = TboutWork.objects.get(ow_number=ow_number)
        i = Tbapplication.objects.filter(stu=student).filter(ow_number=ow_number).filter(apply_status="已录用").get(s_sure="已确认")
        interviewApply = TbinterviewApply.objects.get(ow_number=i.ow_number)
        interviewNotice = TbinterviewNotice.objects.get(ia_number=interviewApply.ia_number)
        interviewResult = TbinterviewResult.objects.get(i_number=interviewNotice)
        address = i.ow_number.w_place + i.ow_number.w_place_detail
        plays.append({'type': "校外兼职", 'ow_number': i.ow_number.ow_number, 'post': i.ow_number.ow_post,
                      'time': interviewResult.ir_rtime, 'address': address, 'ps': interviewResult.ir_ps,
                      'success': True, 'fail': False})
    else:
        iw_number = TbinWork.objects.get(iw_number=iw_number)
        i = Tbapplication.objects.filter(stu=student).filter(iw_number=iw_number).filter(apply_status="已录用").get(
            s_sure="已确认")
        inResult = TbinResult.objects.get(iw_number =i.iw_number)
        plays.append({'type':"校内兼职",'iw_number': i.iw_number.iw_number, 'post': i.iw_number.iw_post,
                          'phonenum': inResult.inr_phonenum,'ps': inResult.r_ps,'success':True,'fail':False})
    plays_json = json.dumps(plays, ensure_ascii=False)
    return HttpResponse(plays_json)

#sjieguotongzhi 学生工作结果确认
def Stu_result_sure(request):
    if request.method == "POST":
        type = request.POST.get('type')
        stu_id = request.POST.get('user')
        student = Tbstudent.objects.get(stu_id=stu_id)
        number = request.POST.get('number')
        if type == "校内兼职":
            iw_number = TbinWork.objects.get(iw_number=number)
            Tbapplication.objects.filter(stu=student).filter(iw_number=iw_number).update(s_sure="已确认")
            views01.in_result_sure(number)
            return HttpResponse("确认成功")
        else:
            ow_number = TboutWork.objects.get(ow_number=number)
            Tbapplication.objects.filter(stu=student).filter(ow_number=ow_number).update(s_sure="已确认")
            views01.out_result_sure(number)
            return HttpResponse("确认成功")
    else:
        return HttpResponse("请求错误")

#sfeedback 学生评价工作
def Stu_feedbackEr(request):
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
            inWork = TbinWork.objects.get(iw_number=iw_number)
            result = TbfeedbackEr.objects.create(fb_content=fb_content, fb_direction='学生评价企业',fb_time=timezone.now(), iw_number=inWork,stu=stu)
            Tbapplication.objects.filter(stu=stu,iw_number=inWork).update(apply_status='已评价')
            views01.in_feedback_over(iw_number)
        else:
            outWork = TboutWork.objects.get(ow_number=ow_number)
            result = TbfeedbackEr.objects.create(fb_content=fb_content, fb_direction='学生评价企业',fb_time=timezone.now(), ow_number=outWork,stu=stu)
            Tbapplication.objects.filter(stu=stu,ow_number=outWork).update(apply_status='已评价')
            views01.out_feedback_over(ow_number)
        result.save()
        return HttpResponse("评价成功")
    else:
        return HttpResponse("请求错误")

#校外评价总显示
def outwork_feedback_com(request):
    ow_number = request.GET.get('ow_number')
    outwork = TboutWork.objects.get(ow_number=ow_number)
    count = 0
    n=0
    worklist = TboutWork.objects.filter(com_number=outwork.com_number)
    for j in worklist:
        feedbackEr = TbfeedbackEr.objects.filter(ow_number=j).filter(fb_direction="学生评价企业")
        for k in feedbackEr:
            b_content0 = k.fb_content.replace("'", '"')
            fb_content = json.loads(b_content0)
            count = count + int(fb_content[0])
            n=n+1
    if count !=0:
        f = count / n
        score = '%.1f' % f #评分
        return HttpResponse(json.dumps({'com_name': outwork.com_number.com_name, 'score': score}))
    else:
        return HttpResponse("该公司暂无评价")

def outwork_feedback_detail(request):
    ow_number = request.GET.get('ow_number')
    outwork = TboutWork.objects.get(ow_number=ow_number)
    feed_content = []
    n=0
    worklist = TboutWork.objects.filter(com_number=outwork.com_number)
    for j in worklist:
        feedbackEr = TbfeedbackEr.objects.filter(ow_number=j).filter(fb_direction="学生评价企业")
        for k in feedbackEr:
            dictionary2 = {}
            dictionary2["name"] = "匿名用户"
            dictionary2["work"] = j.ow_post
            b_content0 = k.fb_content.replace("'", '"')
            fb_content = json.loads(b_content0)
            content = ""
            for i in fb_content:
                if i != fb_content[0] and i != "":
                    content = content + i + ","
            if content == "":
                content = "无评价内容"
            else:
                content = content[:-1]
            n=n+1
            dictionary2["score"] = fb_content[0]
            dictionary2["fb_content"] = content
            dictionary2["fb_time"] = k.fb_time.strftime("%Y-%m-%d, %H:%M:%S")
            feed_content.append(dictionary2)
    if n !=0:
        plays_json = json.dumps(feed_content, ensure_ascii=False)
        return HttpResponse(plays_json)
    else:
        return HttpResponse("该公司暂无评价")

#Salljob 校内外兼职信息展示界面
def Show_work(request):
    type = request.GET.get('type')
    order = request.GET.get('order')
    area = request.GET.get('area')
    plays = []
    if area=="不限":
        area=""
    if type=="校内":
        if order=="综合排序":
            result2 = TbinWork.objects.filter(In_status='报名中')
            for i in result2:
                plays.append(
                    {'type': '校内', 'title': i.iw_post, 'amount': i.w_amount, 'place': i.w_place, 'salary': i.w_salary,
                     'depart': i.iw_depart, 'iw_number': i.iw_number})
        else:
            result2 = TbinWork.objects.filter(In_status='报名中').order_by('inpub_time')
            for i in result2:
                plays.append(
                    {'type': '校内', 'title': i.iw_post, 'amount': i.w_amount, 'place': i.w_place, 'salary': i.w_salary,
                     'depart': i.iw_depart, 'iw_number': i.iw_number})
    else:
        if type=="不限":
            if order == "综合排序":
                result1 = TboutWork.objects.filter(ow_status='报名中').filter(w_place=area)
                result2 = TbinWork.objects.filter(In_status='报名中')
                for i in result1:
                    user = TboutWork.objects.get(ow_number=i.ow_number)
                    com_number = user.com_number.com_number
                    com_name = Tbcompany.objects.get(com_number=com_number).com_name
                    plays.append(
                        {'type': '校外', 'title': i.ow_post, 'amount': i.w_amount, 'place': i.w_place, 'salary': i.w_salary,
                            'depart': com_name, 'iw_number': 'NULL', 'ow_number': i.ow_number})
                for i in result2:
                    plays.append(
                        {'type': '校内', 'title': i.iw_post, 'amount': i.w_amount, 'place': i.w_place,
                         'salary': i.w_salary,
                         'depart': i.iw_depart, 'iw_number': i.iw_number})
            else:
                result1 = TboutWork.objects.filter(ow_status='报名中').filter(w_place=area).order_by('ipub_time')
                result2 = TbinWork.objects.filter(In_status='报名中').order_by('inpub_time')
                for i in result1:
                    user = TboutWork.objects.get(ow_number=i.ow_number)
                    com_number = user.com_number.com_number
                    com_name = Tbcompany.objects.get(com_number=com_number).com_name
                    plays.append(
                        {'type': '校外', 'title': i.ow_post, 'amount': i.w_amount, 'place': i.w_place, 'salary': i.w_salary,
                            'depart': com_name, 'iw_number': 'NULL', 'ow_number': i.ow_number})
                for i in result2:
                    plays.append(
                        {'type': '校内', 'title': i.iw_post, 'amount': i.w_amount, 'place': i.w_place,
                         'salary': i.w_salary,
                         'depart': i.iw_depart, 'iw_number': i.iw_number})
        else:
            if order == "综合排序":
                result1 = TboutWork.objects.filter(ow_status='报名中').filter(w_place=area)
                for i in result1:
                    user = TboutWork.objects.get(ow_number=i.ow_number)
                    com_number = user.com_number.com_number
                    com_name = Tbcompany.objects.get(com_number=com_number).com_name
                    plays.append(
                        {'type': '校外', 'title': i.ow_post, 'amount': i.w_amount, 'place': i.w_place, 'salary': i.w_salary,
                            'depart': com_name, 'iw_number': 'NULL', 'ow_number': i.ow_number})
            else:
                result1 = TboutWork.objects.filter(ow_status='报名中').filter(w_place=area).order_by('ipub_time')
                for i in result1:
                    user = TboutWork.objects.get(ow_number=i.ow_number)
                    com_number = user.com_number.com_number
                    com_name = Tbcompany.objects.get(com_number=com_number).com_name
                    plays.append(
                        {'type': '校外', 'title': i.ow_post, 'amount': i.w_amount, 'place': i.w_place, 'salary': i.w_salary,
                            'depart': com_name, 'iw_number': 'NULL', 'ow_number': i.ow_number})
    plays_json = json.dumps(plays,ensure_ascii=False)
    return HttpResponse(plays_json)

#Salljob 查询类型功能

#Salljob 查询距离功能

#Salljob 查询区域