from django.shortcuts import HttpResponse,render
from django.utils import timezone
from .models import Tbcompany, Tbstudent,Tbresume, Tbqualify, TbinWork, TboutWork, TbinResult, Tbapplication, TbinterviewApply, TbinterviewResult, TbinterviewNotice, TbfeedbackEr, TbfeedbackStu
from django.db.models import Q
from threading import Timer
from django.http import JsonResponse
from . import views01
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
    inwork_list = []
    list = TbinWork.objects.all()
    for i in list:
        dic = {}
        dic["iw_number"] = i.iw_number
        dic["iw_post"] = i.iw_post
        dic["iw_depart"] = i.iw_depart
        dic["w_time"] = i.w_time
        dic["w_place"] = i.w_place
        dic["work"] = i.work
        dic["w_salary"] = i.w_salary
        dic["w_reuire"] = i.w_reuire
        dic["w_amoubt"] = i.w_amount
        dic["ddl_time"] = i.ddl_time
        dic["inpub_time"] = i.inpub_time
        dic["w_ps"] = i.w_ps
        dic["In_status"] = i.In_status
        if dic["In_status"] == "待评价":
            dic["btn_color"] = "button-color4"
        if dic["In_status"] == "报名中":
            dic["btn_color"] = "button-color3"
        if dic["In_status"] == "工作中":
            dic["btn_color"] = "button-color2"
        if dic["In_status"] == "报名结束":
            dic["btn_color"] = "button-color5"
        if dic["In_status"] == "结果通知中":
            dic["btn_color"] = "button-color1"
        if dic["In_status"] == "工作结束":
            dic["btn_color"] = "button-color6"
        if dic["In_status"] == "已结束":
            dic["btn_color"] = "button-color7"
        inwork_list.append(dic)
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
            if dictionary["apply_status"] == "待审核":
                dictionary["btn_color"] = "button-color4"
            if dictionary["apply_status"] == "面试通知中":
                dictionary["btn_color"] = "button-color3"
            if dictionary["apply_status"] == "已打回":
                dictionary["btn_color"] = "button-color5"
            if dictionary["apply_status"] == "面试阶段":
                dictionary["btn_color"] = "button-color6"
            if outwork.ow_status != "面试申请中":
                interviewNotice = TbinterviewNotice.objects.get(ia_number=i.ia_number)
                dictionary["c_sure"] = interviewNotice.c_sure
            else:
                dictionary["c_sure"] = "未开启"
            if dictionary["c_sure"] == "未开启":
                dictionary["btn_colors"] = "button-color3"
            if dictionary["c_sure"] == "未确认":
                dictionary["btn_colors"] = "button-color5"
            if dictionary["c_sure"] == "已确认":
                dictionary["btn_colors"] = "button-color2"
            interview_list.append(dictionary)
    return render(request, 'wechat/interview_list.html', {'interview_list': interview_list})

#校外应聘学生查看
def stu_yingpin(request):
    ia_number = request.GET.get("yp_num")
    interviewApply = TbinterviewApply.objects.get(ia_number=ia_number)
    outwork = interviewApply.ow_number
    list1 = Tbapplication.objects.filter(ow_number=outwork.ow_number).exclude(apply_status = "表筛未通过")
    list2 = Tbapplication.objects.filter(ow_number=outwork.ow_number).filter(apply_status="表筛未通过")
    stu_yingpinlist = []
    for i in list1:
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
        if outwork.ow_status == "面试通知中" or outwork.ow_status == "面试申请中":
            dictionary["s_sure"] = "未开启"
        else:
            interviewNotice = TbinterviewNotice.objects.get(ia_number=ia_number)
            stu = interviewNotice.stu.replace("'", '"')
            stu = json.loads(stu)
            s_sure = interviewNotice.s_sure.replace("'", '"')
            s_sure = json.loads(s_sure)
            k=0
            for i in stu:
                if i == stu_id:
                    dictionary["s_sure"] = s_sure[k]
                k = k + 1
        stu_yingpinlist.append(dictionary)
    for i in list2:
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
        dictionary["s_sure"] = "未开启"
        stu_yingpinlist.append(dictionary)
    return render(request, 'wechat/stu_yingpin.html', {'stu_yingpinlist': stu_yingpinlist})

#面试信息通知界面
def interview_notice_send(request):
    ia_number = request.GET.get("result_num")
    interviewApply = TbinterviewApply.objects.get(ia_number=ia_number)
    outwork = interviewApply.ow_number
    if (outwork.ow_status == "面试申请中" or outwork.ow_status == "面试通知中") and interviewApply.apply_status !="已打回":
        filterResult = TbinterviewNotice.objects.filter(ia_number=ia_number)
        if len(filterResult) > 0:
            interviewNotice = TbinterviewNotice.objects.get(ia_number=ia_number)
            i_com = outwork.com_number.com_name
            k=0
            stu= interviewNotice.stu.replace("'",'"')
            stu=json.loads(stu)   #str转化为list,便于数据库取数据
            for j in stu:
                k=k+1
            i_num = str(k)+"人"
            if interviewNotice.i_address is None:
                i_address = ""
            else:
                i_address = interviewNotice.i_address
            return render(request, 'wechat/notice_send.html', {'i_number': interviewNotice.i_number, 'ia_number': interviewNotice.ia_number, 'i_com': i_com,
                 'i_num': i_num, 'in_time': interviewNotice.in_time, 'i_address': i_address})
        else:
            apply = Tbapplication.objects.filter(ow_number=outwork.ow_number).filter(apply_status="表筛通过")
            stu = []
            k = 0
            for i in apply:
                id=i.stu.stu_id
                stu.append(id)
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
    if request.method == "POST":
        i_number = request.POST.get('i_number')
        in_time = request.POST.get('in_time')
        i_address = request.POST.get('i_address')
        i_com = request.POST.get('i_com')
        TbinterviewNotice.objects.filter(i_number=i_number).update(in_time=in_time,i_address=i_address)
        interviewNotice = TbinterviewNotice.objects.get(i_number=i_number)
        i_com = i_com
        k = 0
        stu = interviewNotice.stu.replace("'", '"')
        stu = json.loads(stu)  # str转化为list,便于数据库取数据
        for j in stu:
            k = k + 1
        i_num = str(k) + "人"
        return render(request, 'wechat/notice_send.html',
                      {'i_number': interviewNotice.i_number, 'ia_number': interviewNotice.ia_number, 'i_com': i_com,
                       'i_num': i_num, 'in_time': interviewNotice.in_time, 'i_address': interviewNotice.i_address})

#面试信息通知界面(发送按钮）
def interview_notice_send_send(request):
    i_number = request.GET.get('send_num')
    interviewNotice = TbinterviewNotice.objects.get(i_number=i_number)
    interviewApply = TbinterviewApply.objects.get(ia_number=interviewNotice.ia_number)
    ow_number = interviewApply.ow_number.ow_number
    TboutWork.objects.filter(ow_number=ow_number).update(ow_status='面试通知中')
    stu = interviewNotice.stu.replace("'", '"')
    stu = json.loads(stu)
    s_sure =[]
    for j in stu:
        s_sure.append("未确认")
        student = Tbstudent.objects.get(stu_id=j)
        Tbapplication.objects.filter(ow_number=ow_number).filter(stu=student).update(apply_status="面试中")
    TbinterviewNotice.objects.filter(i_number=i_number).update(s_sure=s_sure)
    TbinterviewApply.objects.filter(ia_number=interviewNotice.ia_number).update(apply_status="面试通知中")
    #结果界面导入
    interview_list = []
    list = TbinterviewApply.objects.all()
    for i in list:
        outwork = i.ow_number
        if outwork.ow_status == "面试申请中" or outwork.ow_status == "面试通知中" or outwork.ow_status == "面试阶段":
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

#面试信息打回界面
def interview_back_reason(request):
    ia_number = request.GET.get('ia_num')
    interviewApply = TbinterviewApply.objects.get(ia_number=ia_number)
    outwork = interviewApply.ow_number
    if interviewApply.apply_status == "待审核" or interviewApply.apply_status == "已打回":
        c_phonenum = interviewApply.phonenumber
        if interviewApply.back_reason is None:
            back_reason = ""
        else:
            back_reason = interviewApply.back_reason
        return render(request, 'wechat/back_reason.html', {'ow_number': outwork.ow_number,'ia_number':ia_number,'c_phonenum':c_phonenum,'back_reason': back_reason})
    else:
        return render(request, 'wechat/manage_error.html')

#校外兼职打回理由生成(保存按钮）
def interview_back_reason_save(request):
    if request.method == "POST":
        ia_number = request.POST.get('ia_number')
        back_reason = request.POST.get('back_reason')
        TbinterviewApply.objects.filter(ia_number=ia_number).update(back_reason= back_reason)
        interviewApply = TbinterviewApply.objects.get(ia_number=ia_number)
        outwork = interviewApply.ow_number
        c_phonenum = interviewApply.phonenumber
        return render(request, 'wechat/back_reason.html', {'ow_number': outwork.ow_number,'ia_number':ia_number,'c_phonenum':c_phonenum,'back_reason': back_reason})
    else:
        return HttpResponse("请求错误")

# 校外兼职打回理由生成(发送按钮）
def interview_back_reason_send(request):
    ia_number = request.GET.get('submit_num')
    TbinterviewApply.objects.filter(ia_number=ia_number).update(apply_status="已打回")
    # 结果界面导入
    interview_list = []
    list = TbinterviewApply.objects.all()
    for i in list:
        outwork = i.ow_number
        if outwork.ow_status == "面试申请中" or outwork.ow_status == "面试通知中" or outwork.ow_status == "面试阶段":
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

#面试结果界面
def interview_result(request):
    interview_result=[]
    list = TbinterviewResult.objects.all()
    for i in list:
        interviewNotice = i.i_number
        interviewApply = TbinterviewApply.objects.get(ia_number=interviewNotice.ia_number)
        outwork = interviewApply.ow_number
        if outwork.ow_status == "结果通知中" or outwork.ow_status == "工作中"or outwork.ow_status == "待评价"or outwork.ow_status == "已结束"or outwork.ow_status == "工作结束":
            dictionary = {}
            dictionary["ir_number"] = i.ir_number
            dictionary["ow_number"] = outwork.ow_number
            dictionary["i_number"] = i.i_number.i_number
            dictionary["ir_rtime"] = i.ir_rtime
            dictionary["ir_address"] = outwork.w_place + outwork.w_place_detail
            result = i.ir_result.replace("'", '"')
            result = json.loads(result)  # str转化为list,便于数据库取数据
            k=0
            for j in result:
                k = k + 1
            dictionary["i_num"] = str(k) + "人"
            dictionary["ir_ps"] = i.ir_ps
            dictionary["ow_status"] = outwork.ow_status
            if dictionary["ow_status"] == "结果通知中":
                dictionary["btn_color"] = "button-color3"
            if dictionary["ow_status"] == "工作中":
                dictionary["btn_color"] = "button-color2"
            if dictionary["ow_status"] == "待评价":
                dictionary["btn_color"] = "button-color4"
            if dictionary["ow_status"] == "已结束":
                dictionary["btn_color"] = "button-color5"
            interview_result.append(dictionary)
    return render(request, 'wechat/interview_result.html', {'interview_result': interview_result})

#面试录用详情界面
def interview_stu_result(request):
    i_number = request.GET.get('i_num')
    interviewNotice = TbinterviewNotice.objects.get(i_number=i_number)
    interviewApply = TbinterviewApply.objects.get(ia_number=interviewNotice.ia_number)
    outwork = interviewApply.ow_number
    stu = interviewNotice.stu.replace("'", '"')
    stu = json.loads(stu)  # str转化为list,便于数据库取数据
    stu_result = []
    for j in stu:
        student = Tbstudent.objects.get(stu_id=j)
        dictionary = {}
        dictionary["stu_id"] = student.stu_id
        dictionary["name"] = student.name
        dictionary["sex"] = student.sex
        dictionary["phonenumber"] = student.phonenumber_phonenumberphonenumber_phonenumber
        dictionary["grade"] = student.grade
        application = Tbapplication.objects.filter(ow_number=outwork).get(stu=student)
        dictionary["apply_status"] = application.apply_status
        if dictionary["apply_status"] == "未录用":
            dictionary["s_sure"] = "未开启"
        else:
            dictionary["s_sure"] = application.s_sure
        stu_result.append(dictionary)
    return render(request, 'wechat/stu_result.html', {'stu_result': stu_result})

#校内兼职学生评价
#评价学生管理总列表
def stu_feedback_list(request):
    stu_feedback_list = []
    list1 = TbinWork.objects.filter(Q(In_status="已结束") | Q(In_status="工作中") | Q(In_status="待评价")| Q(In_status="工作结束"))
    for i in list1:
        inResult = TbinResult.objects.get(iw_number=i)
        dictionary1 = {}
        dictionary1["iw_number"] = i.iw_number
        dictionary1["work"] = i.iw_post
        dictionary1["inr_phonenum"] = inResult.inr_phonenum
        dictionary1["stu_list"] = []
        list2 = Tbapplication.objects.filter(iw_number=i)
        dictionary1["name"] = list2[0].stu.name
        dictionary1["stu_id"] = list2[0].stu.stu_id
        if i.In_status == "工作中":
            dictionary1["stu_pingjia"] = "未开启"
            dictionary1["pingjia"] = "未开启"
            dictionary1["btn_color1"] = "button-color5"
            dictionary1["btn_color2"] = "button-color5"
        else:
            dictionary1["stu_pingjia"] = list2[0].apply_status
            fb_direction = "企业评价学生"
            filterResult = TbfeedbackEr.objects.filter(stu=list2[0].stu).filter(iw_number=i).filter(fb_direction=fb_direction)
            if len(filterResult) > 0:
                dictionary1["pingjia"] = "已评价"
                dictionary1["btn_color1"] = "button-color2"
            else:
                dictionary1["pingjia"] = "请评价"
                dictionary1["btn_color1"] = "button-color6"
        dictionary1["num"] = str(len(list2))
        list3 = Tbapplication.objects.filter(iw_number=i).exclude(stu=list2[0].stu)
        for j in list3:
            dictionary2 = {}
            dictionary2["name"] = j.stu.name
            dictionary2["stu_id"] = j.stu.stu_id
            if i.In_status == "工作中":
                dictionary2["stu_pingjia"] = "未开启"
                dictionary2["pingjia"] = "未开启"
            else:
                dictionary2["stu_pingjia"] = j.apply_status
                fb_direction="企业评价学生"
                filterResult = TbfeedbackEr.objects.filter(stu=j.stu).filter(iw_number=i).filter(fb_direction=fb_direction)
                if len(filterResult) > 0:
                    dictionary2["pingjia"] = "已评价"
                else:
                    dictionary2["pingjia"] = "请评价"

            if dictionary2["pingjia"] == "未开启":
                dictionary2["btn_color2"] = "button-color3"
            if dictionary2["pingjia"] == "待评价":
                dictionary2["btn_color2"] = "button-color4"
            if dictionary2["pingjia"] == "已评价":
                dictionary2["btn_color2"] = "button-color2"
            if dictionary2["stu_pingjia"] == "未开启":
                dictionary2["btn_color1"] = "button-color3"
            if dictionary2["stu_pingjia"] == "待评价":
                dictionary2["btn_color1"] = "button-color4"
            if dictionary2["stu_pingjia"] == "已评价":
                dictionary2["btn_color1"] = "button-color2"
            dictionary1["stu_list"].append(dictionary2)
        dictionary1["in_status"] = i.In_status
        if dictionary1["in_status"] == "已结束":
            dictionary1["btn_color"] = "button-color5"
        if dictionary1["in_status"] == "工作中":
            dictionary1["btn_color"] = "button-color2"
        if dictionary1["in_status"] == "待评价":
            dictionary1["btn_color"] = "button-color3"
        if dictionary1["in_status"] == "工作结束":
            dictionary1["btn_color"] = "button-color4"

        if dictionary1["pingjia"] == "未开启":
            dictionary1["btn_color2"] = "button-color3"
        if dictionary1["pingjia"] == "待评价":
            dictionary1["btn_color2"] = "button-color4"
        if dictionary1["pingjia"] == "已评价":
            dictionary1["btn_color2"] = "button-color2"
        if dictionary1["stu_pingjia"] == "未开启":
            dictionary1["btn_color1"] = "button-color3"
        if dictionary1["stu_pingjia"] == "待评价":
            dictionary1["btn_color1"] = "button-color4"
        if dictionary1["stu_pingjia"] == "已评价":
            dictionary1["btn_color1"] = "button-color2"
        stu_feedback_list.append(dictionary1)
    return render(request, 'wechat/stu_feedback.html', {'stu_feedback_list': stu_feedback_list})

#校内工作结束
def management_inWork_end(request):
    iw_number = request.GET.get('finish_num')
    inWork=TbinWork.objects.get(iw_number=iw_number)
    if inWork.In_status == "工作中":
        TbinWork.objects.filter(iw_number=iw_number).update(In_status="工作结束")
        Tbapplication.objects.filter(iw_number=inWork).filter(apply_status="已录用").update(apply_status="工作结束")
        stu_feedback_list = []
        list1 = TbinWork.objects.filter(
            Q(In_status="已结束") | Q(In_status="工作中") | Q(In_status="待评价") | Q(In_status="工作结束"))
        for i in list1:
            inResult = TbinResult.objects.get(iw_number=i)
            dictionary1 = {}
            dictionary1["iw_number"] = i.iw_number
            dictionary1["work"] = i.iw_post
            dictionary1["inr_phonenum"] = inResult.inr_phonenum
            dictionary1["stu_list"] = []
            list2 = Tbapplication.objects.filter(iw_number=i)
            dictionary1["name"] = list2[0].stu.name
            dictionary1["stu_id"] = list2[0].stu.stu_id
            if i.In_status == "工作中":
                dictionary1["stu_pingjia"] = "未开启"
                dictionary1["pingjia"] = "未开启"
                dictionary1["btn_color1"] = "button-color5"
                dictionary1["btn_color2"] = "button-color5"
            else:
                dictionary1["stu_pingjia"] = list2[0].apply_status
                fb_direction = "企业评价学生"
                filterResult = TbfeedbackEr.objects.filter(stu=list2[0].stu).filter(iw_number=i).filter(
                    fb_direction=fb_direction)
                if len(filterResult) > 0:
                    dictionary1["pingjia"] = "已评价"
                    dictionary1["btn_color1"] = "button-color2"
                else:
                    dictionary1["pingjia"] = "请评价"
                    dictionary1["btn_color1"] = "button-color6"
            dictionary1["num"] = str(len(list2))
            list3 = Tbapplication.objects.filter(iw_number=i).exclude(stu=list2[0].stu)
            for j in list3:
                dictionary2 = {}
                dictionary2["name"] = j.stu.name
                dictionary2["stu_id"] = j.stu.stu_id
                if i.In_status == "工作中":
                    dictionary2["stu_pingjia"] = "未开启"
                    dictionary2["pingjia"] = "未开启"
                else:
                    dictionary2["stu_pingjia"] = j.apply_status
                    fb_direction = "企业评价学生"
                    filterResult = TbfeedbackEr.objects.filter(stu=j.stu).filter(iw_number=i).filter(
                        fb_direction=fb_direction)
                    if len(filterResult) > 0:
                        dictionary2["pingjia"] = "已评价"
                    else:
                        dictionary2["pingjia"] = "请评价"

                if dictionary2["pingjia"] == "未开启":
                    dictionary2["btn_color2"] = "button-color3"
                if dictionary2["pingjia"] == "待评价":
                    dictionary2["btn_color2"] = "button-color4"
                if dictionary2["pingjia"] == "已评价":
                    dictionary2["btn_color2"] = "button-color2"
                if dictionary2["stu_pingjia"] == "未开启":
                    dictionary2["btn_color1"] = "button-color3"
                if dictionary2["stu_pingjia"] == "待评价":
                    dictionary2["btn_color1"] = "button-color4"
                if dictionary2["stu_pingjia"] == "已评价":
                    dictionary2["btn_color1"] = "button-color2"
                dictionary1["stu_list"].append(dictionary2)
            dictionary1["in_status"] = i.In_status
            if dictionary1["in_status"] == "已结束":
                dictionary1["btn_color"] = "button-color5"
            if dictionary1["in_status"] == "工作中":
                dictionary1["btn_color"] = "button-color2"
            if dictionary1["in_status"] == "待评价":
                dictionary1["btn_color"] = "button-color3"
            if dictionary1["in_status"] == "工作结束":
                dictionary1["btn_color"] = "button-color4"

            if dictionary1["pingjia"] == "未开启":
                dictionary1["btn_color2"] = "button-color3"
            if dictionary1["pingjia"] == "待评价":
                dictionary1["btn_color2"] = "button-color4"
            if dictionary1["pingjia"] == "已评价":
                dictionary1["btn_color2"] = "button-color2"
            if dictionary1["stu_pingjia"] == "未开启":
                dictionary1["btn_color1"] = "button-color3"
            if dictionary1["stu_pingjia"] == "待评价":
                dictionary1["btn_color1"] = "button-color4"
            if dictionary1["stu_pingjia"] == "已评价":
                dictionary1["btn_color1"] = "button-color2"
            stu_feedback_list.append(dictionary1)
        return render(request, 'wechat/stu_feedback.html', {'stu_feedback_list': stu_feedback_list})
    else:
        return render(request, 'wechat/manage_error.html')

#校内工作结算
def management_inWork_paid(request):
    iw_number = request.GET.get('finish_num')
    inWork=TbinWork.objects.get(iw_number=iw_number)
    if inWork.In_status == "工作结束":
        TbinWork.objects.filter(iw_number=iw_number).update(In_status="待评价")
        Tbapplication.objects.filter(iw_number=inWork).filter(apply_status="工作结束").update(apply_status="待评价")
        stu_feedback_list = []
        list1 = TbinWork.objects.filter(
            Q(In_status="已结束") | Q(In_status="工作中") | Q(In_status="待评价") | Q(In_status="工作结束"))
        for i in list1:
            inResult = TbinResult.objects.get(iw_number=i)
            dictionary1 = {}
            dictionary1["iw_number"] = i.iw_number
            dictionary1["work"] = i.iw_post
            dictionary1["inr_phonenum"] = inResult.inr_phonenum
            dictionary1["stu_list"] = []
            list2 = Tbapplication.objects.filter(iw_number=i)
            dictionary1["name"] = list2[0].stu.name
            dictionary1["stu_id"] = list2[0].stu.stu_id
            if i.In_status == "工作中":
                dictionary1["stu_pingjia"] = "未开启"
                dictionary1["pingjia"] = "未开启"
                dictionary1["btn_color1"] = "button-color5"
                dictionary1["btn_color2"] = "button-color5"
            else:
                dictionary1["stu_pingjia"] = list2[0].apply_status
                fb_direction = "企业评价学生"
                filterResult = TbfeedbackEr.objects.filter(stu=list2[0].stu).filter(iw_number=i).filter(
                    fb_direction=fb_direction)
                if len(filterResult) > 0:
                    dictionary1["pingjia"] = "已评价"
                    dictionary1["btn_color1"] = "button-color2"
                else:
                    dictionary1["pingjia"] = "请评价"
                    dictionary1["btn_color1"] = "button-color6"
            dictionary1["num"] = str(len(list2))
            list3 = Tbapplication.objects.filter(iw_number=i).exclude(stu=list2[0].stu)
            for j in list3:
                dictionary2 = {}
                dictionary2["name"] = j.stu.name
                dictionary2["stu_id"] = j.stu.stu_id
                if i.In_status == "工作中":
                    dictionary2["stu_pingjia"] = "未开启"
                    dictionary2["pingjia"] = "未开启"
                else:
                    dictionary2["stu_pingjia"] = j.apply_status
                    fb_direction = "企业评价学生"
                    filterResult = TbfeedbackEr.objects.filter(stu=j.stu).filter(iw_number=i).filter(
                        fb_direction=fb_direction)
                    if len(filterResult) > 0:
                        dictionary2["pingjia"] = "已评价"
                    else:
                        dictionary2["pingjia"] = "请评价"

                if dictionary2["pingjia"] == "未开启":
                    dictionary2["btn_color2"] = "button-color3"
                if dictionary2["pingjia"] == "待评价":
                    dictionary2["btn_color2"] = "button-color4"
                if dictionary2["pingjia"] == "已评价":
                    dictionary2["btn_color2"] = "button-color2"
                if dictionary2["stu_pingjia"] == "未开启":
                    dictionary2["btn_color1"] = "button-color3"
                if dictionary2["stu_pingjia"] == "待评价":
                    dictionary2["btn_color1"] = "button-color4"
                if dictionary2["stu_pingjia"] == "已评价":
                    dictionary2["btn_color1"] = "button-color2"
                dictionary1["stu_list"].append(dictionary2)
            dictionary1["in_status"] = i.In_status
            if dictionary1["in_status"] == "已结束":
                dictionary1["btn_color"] = "button-color5"
            if dictionary1["in_status"] == "工作中":
                dictionary1["btn_color"] = "button-color2"
            if dictionary1["in_status"] == "待评价":
                dictionary1["btn_color"] = "button-color3"
            if dictionary1["in_status"] == "工作结束":
                dictionary1["btn_color"] = "button-color4"

            if dictionary1["pingjia"] == "未开启":
                dictionary1["btn_color2"] = "button-color3"
            if dictionary1["pingjia"] == "待评价":
                dictionary1["btn_color2"] = "button-color4"
            if dictionary1["pingjia"] == "已评价":
                dictionary1["btn_color2"] = "button-color2"
            if dictionary1["stu_pingjia"] == "未开启":
                dictionary1["btn_color1"] = "button-color3"
            if dictionary1["stu_pingjia"] == "待评价":
                dictionary1["btn_color1"] = "button-color4"
            if dictionary1["stu_pingjia"] == "已评价":
                dictionary1["btn_color1"] = "button-color2"
            stu_feedback_list.append(dictionary1)
        return render(request, 'wechat/stu_feedback.html', {'stu_feedback_list': stu_feedback_list})
    else:
        return render(request, 'wechat/manage_error.html')

#校内编辑学生评价
def stu_feedback_edit(request):
    fd_list = request.GET.get('fd_list')
    local1 =fd_list.rfind(",")+1
    local2 = fd_list.rfind(",",0,15)+1
    local3 = local1-1
    pingjia =fd_list[local1:]
    pingjia =pingjia.replace("]","")
    iw_number = fd_list[local2:local3]
    stu_id = fd_list[1:14]
    inWork = TbinWork.objects.get(iw_number=iw_number)
    stu =Tbstudent.objects.get(stu_id=stu_id)
    if pingjia =="请评价":
        return render(request, 'wechat/stu_feedback_edit.html', {'stu_id': stu_id,'name': stu.name,'work': inWork.iw_post,'iw_number':iw_number})
    if pingjia =="已评价":
        feedbackEr = TbfeedbackEr.objects.filter(stu =stu).filter(iw_number =inWork).get(fb_direction="企业评价学生")
        b_content0 = feedbackEr.fb_content.replace("'",'"')
        fb_content = json.loads(b_content0)
        content =""
        for i in fb_content:
            if i != fb_content[0] and i !="":
                content = content + i +","
        if content =="":
            content = "无评价内容"
        else:
            content = content[:-1]
        return render(request, 'wechat/stu_feedback_edit_show.html',
                      {'stu_id': stu_id, 'name': stu.name, 'work': inWork.iw_post, "score" : fb_content[0] , "content" : content, "time":str(feedbackEr.fb_time)})
    if pingjia =="未开启":
        return render(request, 'wechat/manage_feedback_error.html')

#校内编辑学生评价提交
def stu_feedback_edit_save(request):
    if request.method == "POST":
        stu_id = request.POST.get('stu_id')
        iw_number = request.POST.get('iw_number')
        score = request.POST.get('score')
        class1 = request.POST.get('class1')
        class2 = request.POST.get('class2')
        class3 = request.POST.get('class3')
        class4 = request.POST.get('class4')
        class5 = request.POST.get('class5')
        content = request.POST.get('fb_content')
        fb_content = []
        fb_content.append(score)
        if class1 is not None:
            fb_content.append(class1)
        else:
            fb_content.append("")
        if class2 is not None:
            fb_content.append(class2)
        else:
            fb_content.append("")
        if class3 is not None:
            fb_content.append(class3)
        else:
            fb_content.append("")
        if class4 is not None:
            fb_content.append(class4)
        else:
            fb_content.append("")
        if class5 is not None:
            fb_content.append(class5)
        else:
            fb_content.append("")
        fb_content.append(content)
        stu = Tbstudent.objects.get(stu_id=stu_id)
        inWork = TbinWork.objects.get(iw_number=iw_number)
        result = TbfeedbackEr.objects.create(fb_content=fb_content, fb_direction='企业评价学生', fb_time=timezone.now(),
                                             iw_number=inWork, stu=stu)
        views01.in_feedback_over(iw_number)
        result.save()
        stu_feedback_list = []
        list1 = TbinWork.objects.filter(
            Q(In_status="已结束") | Q(In_status="工作中") | Q(In_status="待评价") | Q(In_status="工作结束"))
        for i in list1:
            inResult = TbinResult.objects.get(iw_number=i)
            dictionary1 = {}
            dictionary1["iw_number"] = i.iw_number
            dictionary1["work"] = i.iw_post
            dictionary1["inr_phonenum"] = inResult.inr_phonenum
            dictionary1["stu_list"] = []
            list2 = Tbapplication.objects.filter(iw_number=i)
            dictionary1["name"] = list2[0].stu.name
            dictionary1["stu_id"] = list2[0].stu.stu_id
            if i.In_status == "工作中":
                dictionary1["stu_pingjia"] = "未开启"
                dictionary1["pingjia"] = "未开启"
                dictionary1["btn_color1"] = "button-color5"
                dictionary1["btn_color2"] = "button-color5"
            else:
                dictionary1["stu_pingjia"] = list2[0].apply_status
                fb_direction = "企业评价学生"
                filterResult = TbfeedbackEr.objects.filter(stu=list2[0].stu).filter(iw_number=i).filter(
                    fb_direction=fb_direction)
                if len(filterResult) > 0:
                    dictionary1["pingjia"] = "已评价"
                    dictionary1["btn_color1"] = "button-color2"
                else:
                    dictionary1["pingjia"] = "请评价"
                    dictionary1["btn_color1"] = "button-color6"
            dictionary1["num"] = str(len(list2))
            list3 = Tbapplication.objects.filter(iw_number=i).exclude(stu=list2[0].stu)
            for j in list3:
                dictionary2 = {}
                dictionary2["name"] = j.stu.name
                dictionary2["stu_id"] = j.stu.stu_id
                if i.In_status == "工作中":
                    dictionary2["stu_pingjia"] = "未开启"
                    dictionary2["pingjia"] = "未开启"
                else:
                    dictionary2["stu_pingjia"] = j.apply_status
                    fb_direction = "企业评价学生"
                    filterResult = TbfeedbackEr.objects.filter(stu=j.stu).filter(iw_number=i).filter(
                        fb_direction=fb_direction)
                    if len(filterResult) > 0:
                        dictionary2["pingjia"] = "已评价"
                    else:
                        dictionary2["pingjia"] = "请评价"

                if dictionary2["pingjia"] == "未开启":
                    dictionary2["btn_color2"] = "button-color3"
                if dictionary2["pingjia"] == "待评价":
                    dictionary2["btn_color2"] = "button-color4"
                if dictionary2["pingjia"] == "已评价":
                    dictionary2["btn_color2"] = "button-color2"
                if dictionary2["stu_pingjia"] == "未开启":
                    dictionary2["btn_color1"] = "button-color3"
                if dictionary2["stu_pingjia"] == "待评价":
                    dictionary2["btn_color1"] = "button-color4"
                if dictionary2["stu_pingjia"] == "已评价":
                    dictionary2["btn_color1"] = "button-color2"
                dictionary1["stu_list"].append(dictionary2)
            dictionary1["in_status"] = i.In_status
            if dictionary1["in_status"] == "已结束":
                dictionary1["btn_color"] = "button-color5"
            if dictionary1["in_status"] == "工作中":
                dictionary1["btn_color"] = "button-color2"
            if dictionary1["in_status"] == "待评价":
                dictionary1["btn_color"] = "button-color3"
            if dictionary1["in_status"] == "工作结束":
                dictionary1["btn_color"] = "button-color4"

            if dictionary1["pingjia"] == "未开启":
                dictionary1["btn_color2"] = "button-color3"
            if dictionary1["pingjia"] == "待评价":
                dictionary1["btn_color2"] = "button-color4"
            if dictionary1["pingjia"] == "已评价":
                dictionary1["btn_color2"] = "button-color2"
            if dictionary1["stu_pingjia"] == "未开启":
                dictionary1["btn_color1"] = "button-color3"
            if dictionary1["stu_pingjia"] == "待评价":
                dictionary1["btn_color1"] = "button-color4"
            if dictionary1["stu_pingjia"] == "已评价":
                dictionary1["btn_color1"] = "button-color2"
            stu_feedback_list.append(dictionary1)
        return render(request, 'wechat/stu_feedback.html', {'stu_feedback_list': stu_feedback_list})
    else:
        return HttpResponse("请求错误")



#贫困生的兼职查看！！！！