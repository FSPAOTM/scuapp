import datetime
from django.shortcuts import HttpResponse,render
from django.template import loader
from .models import Tbcompany, Tbstudent,Tbresume, Tbqualify,TbinWork,TboutWork,Tbapplication,TbinterviewApply,TbinterviewNotice,TbfeedbackEr,TbinterviewResult
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
import json
from . import views01

from itertools import chain
#以下是企业
#ccenter返回企业名称
def Show_company_name(request):
    if request.method == "POST":
        phone_num = request.POST.get('phone')  #前端从Get_outwork_info界面接收ow_number并存为全局变量
        user = Tbcompany.objects.get(phone_num=phone_num)
        com_name = user.com_name
        return HttpResponse(json.dumps({"name":com_name}))
        #print(json.dumps({"name":com_name}))
    else:
        return HttpResponse("请求错误")
#cinfofill企业信息修改显示功能
def Company_info_showmodiify(request):
    if request.method == "POST":
        phone_num = request.POST.get('phone')  # 唯一标识简历的全局变量
        user = Tbcompany.objects.get(phone_num=phone_num)
        com_License = user.com_License.com_license
        com_name = user.com_name
        com_leader = user.com_leader
        e_mail = user.e_mail
        com_address = user.com_address
        qualify = Tbqualify.objects.get(com_license=com_License)
        com_condition = qualify.com_condition
        com_business = qualify.com_business
        return HttpResponse(json.dumps(
            {"cno": com_License,
             "company": com_name,
             "manname": com_leader,
             "email": e_mail,
             "address": com_address,
             "contents": com_business,
             "condition": com_condition}))
    else:
        return HttpResponse("请求错误")
#cinfofill企业信息修改功能
def Company_info_modiify(request):
    if request.method == "POST":
        com_License = request.POST.get('cno')  # 唯一标识简历的全局变量
        phone_num = request.POST.get('phone')
        com_leader = request.POST.get('manname')
        e_mail = request.POST.get('email')
        com_address = request.POST.get('address')
        com_business = request.POST.get('contents')
        com_condition = request.POST.get('condition')
        Tbcompany.objects.filter(com_License=com_License).update(phone_num=phone_num, com_leader=com_leader, e_mail=e_mail, com_address=com_address)
        Tbqualify.objects.filter(com_license=com_License).update(com_business=com_business, com_condition=com_condition)
        return HttpResponse("填写完成")
    else:
        return HttpResponse("请求错误")
#cjobrelease企业兼职信息发布功能
def Part_time_post(request):
    if request.method == "POST":
        phone_num = request.POST.get('company')
        ow_post = request.POST.get('Name')
        w_time = request.POST.get('jobtime')
        w_place = request.POST.get('location')
        w_place_detail = request.POST.get('detail')
        work = request.POST.get('description')
        w_salary = request.POST.get('salary')
        w_reuire = request.POST.get('ask')
        w_amount = request.POST.get('num')
        ddl_time = request.POST.get('endingtime')
        ipub_time = timezone.now()
        w_ps = request.POST.getlist('ps')
        User = Tbcompany.objects.get(phone_num=phone_num)
        outwork = TboutWork.objects.create(ow_post=ow_post,w_time=w_time,w_place=w_place,w_place_detail=w_place_detail,work=work,w_salary=w_salary,w_reuire=w_reuire,w_amount=w_amount,ddl_time=ddl_time,ipub_time=ipub_time,w_ps=w_ps,com_number=User,ow_status = '待审核')
        outwork.save()
        return HttpResponse("发布成功")
    else:
        return HttpResponse("请求错误")
#cfabu 企业兼职信息展示功能 后期尝试完善在这里传already 未调试
def Get_outwork_info(request):
    phone_num = request.GET.get('user')#获取全局变量
    com = Tbcompany.objects.get(phone_num=phone_num)
    result = TboutWork.objects.filter(com_number=com)#获取对象
    plays = []
    for i in result:
        if i.ow_status =="工作结束":
            plays.append({'ow_number':i.ow_number,'post':i.ow_post,'time':str(i.w_time),'location':i.w_place,'detail':i.w_place_detail,'description':i.work,'salary':i.w_salary,'ask':i.w_reuire,'num':i.w_amount,'ddl':str(i.ddl_time),'ps':i.w_ps,'status':i.ow_status,'show2': True,'show3': False})
        else:
            if i.ow_status =="待评价" or i.ow_status =="已结束":
                plays.append({'ow_number': i.ow_number, 'post': i.ow_post, 'time': str(i.w_time), 'location': i.w_place,
                              'detail': i.w_place_detail, 'description': i.work, 'salary': i.w_salary,
                              'ask': i.w_reuire, 'num': i.w_amount, 'ddl': str(i.ddl_time), 'ps': i.w_ps,
                              'status': i.ow_status, 'show2': False, 'show3': True})
            else:
                plays.append({'ow_number': i.ow_number, 'post': i.ow_post, 'time': str(i.w_time), 'location': i.w_place,
                              'detail': i.w_place_detail, 'description': i.work, 'salary': i.w_salary,
                              'ask': i.w_reuire, 'num': i.w_amount, 'ddl': str(i.ddl_time), 'ps': i.w_ps,
                              'status': i.ow_status})
    plays_json = json.dumps(plays,ensure_ascii=False)
    return HttpResponse(plays_json)
#cfabu 修改工作状态 “工作中” 到 “工作结束” 工作结束按钮
def Get_outwork_info_end(request):
    if request.method == "POST":
        ow_number = request.POST.get('ow_number')
        outwork = TboutWork.objects.get(ow_number=ow_number)
        TboutWork.objects.filter(ow_number=ow_number).update(ow_status="工作结束")
        Tbapplication.objects.filter(ow_number=outwork).filter(apply_status="已录用").update(apply_status="工作结束")
        return HttpResponse("修改成功")
    else:
        return HttpResponse("请求错误")
#cjobshow 企业发布兼职信息展示功能
def Get_outwork_detail_info(request):
    if request.method == "POST":
        ow_number = request.POST.get('ow_number')
        result = TboutWork.objects.get(ow_number=ow_number)
        post = result.ow_post
        time = result.w_time
        location = result.w_place
        detail = result.w_place_detail
        salary = result.w_salary
        description = result.work
        ask = result.w_reuire
        num = result.w_amount
        ddl = str(result.ddl_time)
        ps = result.w_ps
        already = Tbapplication.objects.filter(ow_number=ow_number).count()
        return HttpResponse(json.dumps({
            "post":post,
            "time":time,
            "location":location,
            "detail":detail,
            "salary":salary,
            "description":description,
            "ask":ask,
            "num":num,
            "ddl":ddl,
            "ps":ps,
            "already": already}))
    else:
        return HttpResponse("请求错误")
#cjobshow后的企业兼职信息修改界面
def Modify_outwork_info(request):
    if request.method == "POST":
        ow_number = request.POST.get('ow_number')
        phone_num = request.POST.get('company')
        ow_post = request.POST.get('Name')
        w_time = request.POST.get('jobtime')
        w_place = request.POST.get('location')
        w_place_detail = request.POST.get('detail')
        work = request.POST.get('description')
        w_salary = request.POST.get('salary')
        w_reuire = request.POST.get('ask')
        w_amount = request.POST.get('num')
        ddl_time = request.POST.get('endingtime')
        ipub_time = timezone.now()
        w_ps = request.POST.getlist('ps')
        User = Tbcompany.objects.get(phone_num=phone_num)
        TboutWork.objects.filter(ow_number=ow_number).update(ow_post=ow_post, w_time=w_time, w_place= w_place, w_place_detail=w_place_detail,
                                                             work=work,w_salary=w_salary, w_reuire=w_reuire, w_amount=w_amount, ddl_time=ddl_time,
                                                             ipub_time=ipub_time, w_ps=w_ps, com_number=User, ow_status='待审核')
        return HttpResponse("修改成功")
    else:
        return HttpResponse("请求错误")

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)
#cworkspace 企业端报名者显示功能
def Show_applicant(request):
    if request.method == "GET":
        phone_num = request.GET.get('user')
        com_number = Tbcompany.objects.get(phone_num=phone_num).com_number
        outwork = TboutWork.objects.filter(com_number=com_number)
        plays = []
        for i in outwork:
            ow_post = i.ow_post
            ow_number = i.ow_number
            result = Tbapplication.objects.filter(ow_number=ow_number)
            for item in result:
                ap_time = json.dumps(item.ap_time, cls=DateEncoder)
                plays.append({'ow_number': ow_number,'post': ow_post, 'stu_number': item.stu.stu_id, 'user':item.stu.name, 'status':item.apply_status, 'ap_time':ap_time})
        plays_json = json.dumps(plays, ensure_ascii=False)
        return HttpResponse(plays_json)
    else:
        return HttpResponse("请求错误")
#cresumeReview 点击接受后改变applystatus状态
def Modify_applystatus(request):
    if request.method == "POST":
        stu_id = request.POST.get('stu_number')
        ow_number = request.POST.get('ow_number')
        judge = request.POST.get('status')
        filterResult1 = Tbapplication.objects.filter(stu=stu_id,ow_number=ow_number)
        if len(filterResult1) > 0 and judge=='已通过':
            filterResult1.update(apply_status='表筛通过')
            return HttpResponse("修改成功")
        elif len(filterResult1) > 0 and judge=='未通过':
            filterResult1.update(apply_status='表筛未通过')
            return HttpResponse("修改成功")
        else:
            return HttpResponse("修改失败")
    else:
        return HttpResponse("请求错误")
#cinterview 企业面试申请
@csrf_exempt
def Company_apply_interviewtime(request):
    if request.method == "POST":
        number = request.POST.get('ow_number')
        ia_name = request.POST.get('manager')
        phonenumber = request.POST.get('phonenum')
        applytime1 = request.POST.get('applytime1')
        applytime2 = request.POST.get('applytime2')
        applytime3 = request.POST.get('applytime3')
        a_time = timezone.now()
        ow_number = TboutWork.objects.get(ow_number=number)
        if applytime2 == "" and applytime3 =="":
            ia_time = applytime1
        if applytime2 == "" and applytime3 !="":
            ia_time = applytime1 + "或" + applytime3
        if applytime2 != "" and applytime3 =="":
            ia_time = applytime1 + "或" + applytime2
        if applytime2 != "" and applytime3 !="":
            ia_time = applytime1 + "或" + applytime2+ "或" + applytime3  #考虑存在空时间段
        ow_status = ow_number.ow_status
        list = Tbapplication.objects.filter(ow_number=ow_number)
        k=0
        for i in list:
            if i.apply_status == "待审核":
                k=k+1
        if ow_status=="报名结束" and k == 0 :
            interviewApply = TbinterviewApply.objects.create(ia_time=ia_time,
                                            ia_name=ia_name,
                                            phonenumber=phonenumber,
                                            a_time=a_time,
                                            ow_number=ow_number)
            interviewApply.save()
            TboutWork.objects.filter(ow_number=number).update(ow_status="面试申请中")
            return HttpResponse("提交成功")
        else:
            return HttpResponse("存在学生简历未初步审核,无法申请面试")
    else:
        return HttpResponse("请求错误")
#cmianshitongzhi 企业面试通知显示
def Com_interview_notice_show(request):
    phone_num = request.GET.get('user')
    com = Tbcompany.objects.get(phone_num=phone_num)
    outWork = TboutWork.objects.filter(com_number=com).filter(ow_status="面试通知中")
    plays = []
    for i in outWork:
        interviewApply = TbinterviewApply.objects.get(ow_number=i)
        interviewNotice = TbinterviewNotice.objects.get(ia_number=interviewApply.ia_number)
        if interviewNotice.c_sure =="未确认":
            plays.append({'ow_number': i.ow_number, 'post': i.ow_post, 'time': interviewNotice.in_time, 'place': interviewNotice.i_address})
    plays_json = json.dumps(plays, ensure_ascii=False)
    return HttpResponse(plays_json)
#cmianshitongzhi 企业面试通知确认
def Com_interview_notice_sure(request):
    if request.method == "POST":
        number = request.POST.get('ow_number')
        ow_number = TboutWork.objects.get(ow_number=number)
        interviewApply = TbinterviewApply.objects.get(ow_number=ow_number)
        interviewNotice = TbinterviewNotice.objects.filter(ia_number=interviewApply.ia_number)
        interviewNotice.update(c_sure="已确认")
        views01.interview_sure(interviewNotice[0].i_number)
        return HttpResponse("确认成功")
    else:
        return HttpResponse("请求错误")
#cmianshidahui 企业面试打回理由显示
def Com_interview_back_show(request):
    phone_num = request.GET.get('user')
    com = Tbcompany.objects.get(phone_num=phone_num)
    outWork = TboutWork.objects.filter(com_number=com)
    plays = []
    for i in outWork:
        filterResult = TbinterviewApply.objects.filter(ow_number=i).filter(apply_status="已打回")
        if len(filterResult) >0:
            interviewApply = TbinterviewApply.objects.filter(ow_number=i).get(apply_status="已打回")
            plays.append({'type':"面试申请",'ow_number': i.ow_number, 'post': i.ow_post, 'back_reason': interviewApply.back_reason})
    outWork1 = TboutWork.objects.filter(com_number=com).filter(ow_status="已打回")
    for j in outWork1:
        plays.append({'type': "兼职申请", 'ow_number': j.ow_number, 'post': j.ow_post, 'back_reason': j.back_reason})
    plays_json = json.dumps(plays, ensure_ascii=False)
    return HttpResponse(plays_json)
#cinterviewModify 企业面试申请时间修改显示
def Com_interview_back_edit(request):
    if request.method == "POST":
        number = request.POST.get('ow_number')
        ow_number = TboutWork.objects.get(ow_number=number)
        interviewApply = TbinterviewApply.objects.get(ow_number=ow_number)
        return HttpResponse(json.dumps({'ow_number': number, 'post': ow_number.ow_post, 'manager': interviewApply.ia_name, 'phonenum': interviewApply.phonenumber}))
    else:
        return HttpResponse("请求错误")
#cinterviewModify 企业面试申请重提交
def Com_interview_back_send(request):
    if request.method == "POST":
        number = request.POST.get('ow_number')
        ia_name = request.POST.get('manager')
        phonenumber = request.POST.get('phone')
        applytime1 = request.POST.get('applytime1')
        applytime2 = request.POST.get('applytime2')
        applytime3 = request.POST.get('applytime3')
        a_time = timezone.now()
        ow_number = TboutWork.objects.get(ow_number=number)
        if applytime2 == "" and applytime3 == "":
            ia_time = applytime1
        if applytime2 == "" and applytime3 != "":
            ia_time = applytime1 + "或" + applytime3
        if applytime2 != "" and applytime3 == "":
            ia_time = applytime1 + "或" + applytime2
        if applytime2 != "" and applytime3 != "":
            ia_time = applytime1 + "或" + applytime2 + "或" + applytime3  # 考虑存在空时间段
        TbinterviewApply.objects.filter(ow_number=ow_number).update(ia_time=ia_time,
                                                             ia_name=ia_name,
                                                             phonenumber=phonenumber,
                                                             a_time=a_time,apply_status="待审核")
        return HttpResponse("修改成功")
    else:
        return HttpResponse("请求错误")
#cjobModify 企业工作申请修改显示
def Com_work_back_edit(request):
    if request.method == "POST":
        ow_number = request.POST.get('ow_number')
        outWork = TboutWork.objects.get(ow_number=ow_number)
        return HttpResponse(json.dumps({
            'Name': outWork.ow_post,
            'jobtime': outWork.w_time,
            'location': outWork.w_place,
            'detail': outWork.w_place_detail,
            'description': outWork.work,
            'salary': outWork.w_salary,
            'ask': outWork.w_reuire,
            'num': outWork.w_amount,
            'endingtime': str(outWork.ddl_time),
            'ps': outWork.w_ps}))
    else:
        return HttpResponse("请求错误")
#cresumeReview 企业端简历显示功能
def Com_Insert_resume_show(request):
    if request.method == "POST":
        stu_id = request.POST.get('stuNumber') # 唯一标识简历的全局变量
        ow_number = request.POST.get('ow_number')
        outWork = TboutWork.objects.get(ow_number=ow_number)
        user = Tbstudent.objects.get(stu_id=stu_id)
        res_id = user.res_id.res_id
        resume= Tbresume.objects.get(res_id=res_id)
        name=resume.name
        age=resume.age
        sex=resume.sex
        res_asses=resume.res_asses
        res_edu=resume.res_edu
        res_work=resume.res_work
        res_proj=resume.res_proj
        res_extra=resume.res_extra
        res_per=resume.res_per
        application = Tbapplication.objects.filter(stu=user).get(ow_number=outWork)
        reason = application.ap_reson
        return HttpResponse(json.dumps({
             "name": name,
             "age": age,
             "sex": sex,
             "res_asses": res_asses,
             "res_edu": res_edu,
             "res_work": res_work,
             "res_proj": res_proj,
             "res_extra": res_extra,
             "res_per": res_per,
             "reason": reason}))
    else:
        return HttpResponse("请求错误")

#cfabu 企业端结算工作 已结算按钮 未调试
def Com_work_paid(request):
    if request.method == "POST":
        ow_number = request.POST.get('ow_number')
        outwork = TboutWork.objects.get(ow_number=ow_number)
        TboutWork.objects.filter(ow_number=ow_number).update(ow_status="待评价")
        Tbapplication.objects.filter(ow_number=outwork).filter(apply_status="工作结束").update(apply_status="待评价")
        return HttpResponse("修改成功")
    else:
        return HttpResponse("请求错误")

#cfeedback 企业评价学生 未调试
def Com_feedbackEr(request):
    if request.method == "POST":
        stu = request.POST.get('stuNumber')
        ow_number = request.POST.get('ow_number')
        score = request.POST.get('score')
        serious = request.POST.get('serious')
        manner = request.POST.get('manner')
        timely = request.POST.get('timely')
        labor = request.POST.get('labor')
        ability = request.POST.get('ability')
        more = request.POST.get('more')
        fb_content = []
        fb_content.append(score)
        fb_content.append(serious)
        fb_content.append(timely)
        fb_content.append(manner)
        fb_content.append(labor)
        fb_content.append(ability)
        fb_content.append(more)
        stu = Tbstudent.objects.get(stu_id=stu)
        outWork = TboutWork.objects.get(ow_number=ow_number)
        result = TbfeedbackEr.objects.create(fb_content=fb_content, fb_direction='企业评价学生',fb_time=timezone.now(), ow_number=outWork,stu=stu)
        views01.out_feedback_over(ow_number)
        result.save()
        return HttpResponse("评价成功")
    else:
        return HttpResponse("请求错误")

#cworkspace 企业工作录取结果通知 未调试
def Com_work_employed(request):
    if request.method == "POST":
        mingdan = request.POST.get('mingdan')
        count = request.POST.get('count')
        ir_rtime = request.POST.get('time')
        ir_ps = request.POST.get('ps')
        mingdan = json.loads(mingdan)
        number=[]
        for i in mingdan:
            dict={}
            dict["ow_number"]=i["ow_number"]
            if dict not in number:
                number.append(dict)
        for j in number:
            ir_result=[]
            outwork = TboutWork.objects.get(ow_number=j["ow_number"])
            interviewApply = TbinterviewApply.objects.get(ow_number=outwork)
            interviewNotice = TbinterviewNotice.objects.get(ia_number=interviewApply.ia_number)
            for i in mingdan:
                if i["ow_number"] == j["ow_number"]:
                    stu=Tbstudent.objects.get(stu_id=i["stu_number"])
                    Tbapplication.objects.filter(stu=stu, ow_number=outwork).update(apply_status="已录用")
                    ir_result.append(i["stu_number"])
            interviewResult = TbinterviewResult.objects.create(ir_rtime=ir_rtime,ir_result=ir_result,ir_ps=ir_ps,ir_time=timezone.now(),i_number=interviewNotice)
            interviewResult.save()
            list = Tbapplication.objects.filter(ow_number=outwork)
            k = 0
            for i in list:
                if i.apply_status == "面试中":
                    k = k + 1
            if k == 0:
                TboutWork.objects.filter(ow_number=j["ow_number"]).filter(ow_status="面试阶段").update(ow_status="结果通知中")
        return HttpResponse("通知成功")
    else:
        return HttpResponse("请求错误")

#cworkspace 企业工作未录取结果通知 未调试
def Com_work_unemployed(request):
    if request.method == "POST":
        mingdan = request.POST.get('mingdan')
        count = request.POST.get('count')
        result = mingdan.replace("'", '"')
        mingdan = json.loads(result)
        number=[]
        for i in mingdan:
            dictionary = {}
            dictionary["ow_number"] = i["ow_number"]
            if dictionary not in number:
                number.append(dictionary)
        for j in number:
            outwork = TboutWork.objects.get(ow_number=j["ow_number"])
            for i in mingdan:
                if i["ow_number"] == j["ow_number"]:
                    stu=Tbstudent.objects.get(stu_id=i["stu_number"])
                    Tbapplication.objects.filter(stu=stu, ow_number=outwork).update(apply_status="未录用")
            list = Tbapplication.objects.filter(ow_number=outwork)
            k = 0
            for i in list:
                if i.apply_status == "面试中":
                    k = k + 1
            if k == 0:
                TboutWork.objects.filter(ow_number=j["ow_number"]).filter(ow_status="面试阶段").update(ow_status="结果通知中")
        return HttpResponse("通知成功")
    else:
        return HttpResponse("请求错误")

#评价显示

