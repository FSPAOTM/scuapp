from django.shortcuts import HttpResponse,render
from .models import Tbcompany, Tbstudent,Tbresume, TbinWork, TboutWork, TbinResult, Tbapplication, TbinterviewApply, TbinterviewResult, TbinterviewNotice, TbfeedbackEr,Tbmanager
from django.http import HttpResponseRedirect
import json

#后台管理界面

#用户管理
#学生管理
#学生列表界面（修改）
def stu_manage_list(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
    list = Tbstudent.objects.all()
    stu_list = []
    for i in list:
        dictionary = {}
        dictionary["stu_id"] = i.stu_id
        dictionary["name"] = i.name
        dictionary["res_id"] = i.res_id
        dictionary["nickname"] = i.nickname
        dictionary["phonenumber_phonenumberphonenumber_phonenumber"] = i.phonenumber_phonenumberphonenumber_phonenumber
        if i.sex is not None:
            dictionary["sex"] = i.sex
        else:
            dictionary["sex"] = "未完善"
        if i.age is not None:
            dictionary["age"] = i.age
        else:
            dictionary["age"] = "未完善"
        if i.e_mail is not None:
            dictionary["e_mail"] = i.e_mail
        else:
            dictionary["e_mail"] = "未完善"
        if i.grade is not None:
            dictionary["grade"] = i.grade
        else:
            dictionary["grade"] = "未完善"
        if i.major is not None:
            dictionary["major"] = i.major
        else:
            dictionary["major"] = "未完善"
        if i.pov_identity is not None:
            dictionary["pov_identity"] = i.pov_identity
        else:
            dictionary["pov_identity"] = "未完善"
        stu_list.append(dictionary)
    return render(request, 'wechat/stu_list.html', {'stu_list': stu_list})
#学生工作经历详情界面
def stu_experience(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
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
                    dictionary["end_time"] = feedbackEr1.fb_time.strftime("%Y-%m-%d, %H:%M:%S")
                else:
                    dictionary["end_time"] = "未结束"
            else:
                dictionary["begin_time"] = "未入职"
                dictionary["end_time"] = "未入职"
            if dictionary["In_status"] == "待评价":
                dictionary["btn_color2"] = "button-color4"
            if dictionary["In_status"] == "报名中":
                dictionary["btn_color2"] = "button-color3"
            if dictionary["In_status"] == "工作中":
                dictionary["btn_color2"] = "button-color2"
            if dictionary["In_status"] == "报名结束":
                dictionary["btn_color2"] = "button-color5"
            if dictionary["In_status"] == "结果通知中":
                dictionary["btn_color2"] = "button-color1"
            if dictionary["In_status"] == "工作结束":
                dictionary["btn_color2"] = "button-color6"
            if dictionary["In_status"] == "已结束":
                dictionary["btn_color2"] = "button-color7"

            if dictionary["apply_status"] == "已评价":
                dictionary["btn_color1"] = "button-color2"
            if dictionary["apply_status"] == "已报名":
                dictionary["btn_color1"] = "button-color3"
            if dictionary["apply_status"] == "已录用":
                dictionary["btn_color1"] = "button-color4"
            if dictionary["apply_status"] == "工作结束":
                dictionary["btn_color1"] = "button-color5"
            if dictionary["apply_status"] == "待评价":
                dictionary["btn_color1"] = "button-color1"

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
                            dictionary1["end_time"] = feedbackEr1.fb_time.strftime("%Y-%m-%d, %H:%M:%S")
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
            if dictionary1["ow_status"] == "报名结束":
                dictionary1["btn_color4"] = "button-color5"
            if dictionary1["ow_status"] == "待评价":
                dictionary1["btn_color4"] = "button-color4"
            if dictionary1["ow_status"] == "已打回":
                dictionary1["btn_color4"] = "button-color3"
            if dictionary1["ow_status"] == "结果通知中":
                dictionary1["btn_color4"] = "button-color2"
            if dictionary1["ow_status"] == "面试通知中":
                dictionary1["btn_color4"] = "button-color1"
            if dictionary1["ow_status"] == "面试申请中":
                dictionary1["btn_color4"] = "button-color8"
            if dictionary1["ow_status"] == "工作中":
                dictionary1["btn_color4"] = "button-color7"
            if dictionary1["ow_status"] == "待审核":
                dictionary1["btn_color4"] = "button-color6"
            if dictionary1["ow_status"] == "面试阶段":
                dictionary1["btn_color4"] = "button-color9"
            if dictionary1["ow_status"] == "工作结束":
                dictionary1["btn_color4"] = "button-color10"
            if dictionary1["ow_status"] == "已结束":
                dictionary1["btn_color4"] = "button-color11"
            if dictionary1["ow_status"] == "报名中":
                dictionary1["btn_color4"] = "button-color12"

            if dictionary1["apply_status"] == "表筛未通过":
                dictionary1["btn_color3"] = "button-color5"
            if dictionary1["apply_status"] == "已评价":
                dictionary1["btn_color3"] = "button-color2"
            if dictionary1["apply_status"] == "已录用":
                dictionary1["btn_color3"] = "button-color7"
            if dictionary1["apply_status"] == "工作结束":
                dictionary1["btn_color3"] = "button-color1"
            if dictionary1["apply_status"] == "待评价":
                dictionary1["btn_color3"] = "button-color3"
            if dictionary1["apply_status"] == "面试中":
                dictionary1["btn_color3"] = "button-color1"
            if dictionary1["apply_status"] == "待审核":
                dictionary1["btn_color3"] = "button-color6"
            if dictionary1["apply_status"] == "未录用":
                dictionary1["btn_color3"] = "button-color8"
            stu_outwork.append(dictionary1)
    return render(request, 'wechat/stu_work.html', {'stu_inwork': stu_inwork, 'stu_outwork': stu_outwork})
#学生简历查看界面（界面 emmm)
def stu_manage_resume_list(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
    str = request.GET.get('res_num')
    res_id =str[17:27]
    resume = Tbresume.objects.get(res_id=res_id)
    name = resume.name
    if resume.age is not None:
        age = resume.age
    else:
        age = "未完善"
    if resume.sex is not None:
        sex = resume.sex
    else:
        sex = "未完善"
    if resume.res_asses is not None:
        res_asses = resume.res_asses
    else:
        res_asses = "未完善"
    if resume.res_edu is not None:
        res_edu = resume.res_edu
    else:
        res_edu = "未完善"
    if resume.res_work is not None:
        res_work = resume.res_work
    else:
        res_work = "未完善"
    if resume.res_proj is not None:
        res_proj = resume.res_proj
    else:
        res_proj = "未完善"
    if resume.res_extra is not None:
        res_extra = resume.res_extra
    else:
        res_extra = "未完善"
    if resume.res_per is not None:
        res_per = resume.res_per
    else:
        res_per = "未完善"
    return render(request, 'wechat/stu_resume.html',{"name": name,
             "age": age,
             "sex": sex,
             "res_asses": res_asses,
             "res_edu": res_edu,
             "res_work": res_work,
             "res_proj": res_proj,
             "res_extra": res_extra,
             "res_per": res_per})
#企业管理
#企业列表界面
def company_manage_list(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
    company = Tbcompany.objects.all()
    company_list=[]
    for i in company:
        dictionary = {}
        dictionary["com_number"] = i.com_number
        dictionary["com_name"] = i.com_name
        dictionary["phone_num"] = i.phone_num
        dictionary["com_License"] = i.com_License.com_license
        if i.com_leader is not None:
            dictionary["com_leader"] = i.com_leader
        else:
            dictionary["com_leader"] = "未完善"
        if i.com_address is not None:
            dictionary["com_address"] = i.com_address
        else:
            dictionary["com_address"] = "未完善"
        if i.e_mail is not None:
            dictionary["e_mail"] = i.e_mail
        else:
            dictionary["e_mail"] = "未完善"
        if i.com_License.com_condition is not None:
            dictionary["com_condition"] = i.com_License.com_condition
        else:
            dictionary["com_condition"] = "未完善"
        if i.com_License.com_business is not None:
            dictionary["com_business"] = i.com_License.com_business
        else:
            dictionary["com_business"] = "未完善"
        company_list.append(dictionary)
    return render(request, 'wechat/company_list.html', {'company_list': company_list})
#企业所发布兼职列表
def company_work(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
    com_num = request.GET.get('com_num')
    company = Tbcompany.objects.get(com_number = com_num)
    outwork = TboutWork.objects.filter(com_number = company)
    company_work = []
    for i in outwork:
        dictionary = {}
        dictionary["ow_number"] = i.ow_number
        dictionary["ow_post"] = i.ow_post
        dictionary["w_time"] = i.w_time
        dictionary["w_place"] = i.w_place +i.w_place_detail
        dictionary["work"] = i.work
        dictionary["ipub_time"] = i.ipub_time.strftime("%Y-%m-%d, %H:%M:%S")
        dictionary["ow_status"] = i.ow_status
        if dictionary["ow_status"] == "报名结束":
            dictionary["btn_color4"] = "button-color5"
        if dictionary["ow_status"] == "待评价":
            dictionary["btn_color4"] = "button-color4"
        if dictionary["ow_status"] == "已打回":
            dictionary["btn_color4"] = "button-color3"
        if dictionary["ow_status"] == "结果通知中":
            dictionary["btn_color4"] = "button-color2"
        if dictionary["ow_status"] == "面试通知中":
            dictionary["btn_color4"] = "button-color1"
        if dictionary["ow_status"] == "面试申请中":
            dictionary["btn_color4"] = "button-color8"
        if dictionary["ow_status"] == "工作中":
            dictionary["btn_color4"] = "button-color7"
        if dictionary["ow_status"] == "待审核":
            dictionary["btn_color4"] = "button-color6"
        if dictionary["ow_status"] == "面试阶段":
            dictionary["btn_color4"] = "button-color9"
        if dictionary["ow_status"] == "工作结束":
            dictionary["btn_color4"] = "button-color10"
        if dictionary["ow_status"] == "已结束":
            dictionary["btn_color4"] = "button-color11"
        if dictionary["ow_status"] == "报名中":
            dictionary["btn_color4"] = "button-color12"
        company_work.append(dictionary)
    return render(request, 'wechat/company_work.html', {'company_work': company_work})
#企业兼职录取与招聘情况
def company_employed(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
    ow_number = request.GET.get('ow_number')
    outwork = TboutWork.objects.get(ow_number = ow_number)
    list = Tbapplication.objects.filter(ow_number = outwork)
    company_employed_list = []
    for i in list:
        dictionary = {}
        dictionary["stu_id"] = i.stu.stu_id
        dictionary["name"] = i.stu.name
        dictionary["phonenumber"] = i.stu.phonenumber_phonenumberphonenumber_phonenumber
        dictionary["apply_status"] = i.apply_status
        if dictionary["apply_status"] == "表筛未通过":
            dictionary["btn_color3"] = "button-color5"
        if dictionary["apply_status"] == "已评价":
            dictionary["btn_color3"] = "button-color2"
        if dictionary["apply_status"] == "已录用":
            dictionary["btn_color3"] = "button-color7"
        if dictionary["apply_status"] == "工作结束":
            dictionary["btn_color3"] = "button-color1"
        if dictionary["apply_status"] == "待评价":
            dictionary["btn_color3"] = "button-color3"
        if dictionary["apply_status"] == "面试中":
            dictionary["btn_color3"] = "button-color1"
        if dictionary["apply_status"] == "待审核":
            dictionary["btn_color3"] = "button-color6"
        if dictionary["apply_status"] == "未录用":
            dictionary["btn_color3"] = "button-color8"
        company_employed_list.append(dictionary)
    return render(request, 'wechat/company_employed.html', {'company_employed_list': company_employed_list})
#管理员管理
#管理员列表总界面
def manager_manage_list(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
    manager = Tbmanager.objects.all()
    manager_list=[]
    for i in manager:
        dictionary = {}
        dictionary["manager_id"] = i.manager_id
        dictionary["name"] = i.name
        if i.sex is not None:
            if i.sex =="":
                dictionary["sex"] = "待完善"
            else:
                dictionary["sex"] = i.sex
        else:
            dictionary["sex"] = "待完善"
        dictionary["phonenumber"] = i.phonenumber
        if i.school is not None:
            if i.school =="":
                dictionary["school"] = "待完善"
            else:
                dictionary["school"] = i.school
        else:
            dictionary["school"] = "待完善"
        if i.e_mail is not None:
            if i.e_mail =="":
                dictionary["e_mail"] = "待完善"
            else:
                dictionary["e_mail"] = i.e_mail
        else:
            dictionary["e_mail"] = "待完善"
        manager_list.append(dictionary)
    return render(request, 'wechat/manager_list.html', {'manager_list': manager_list})
#管理员信息完善界面
def manager_ifo(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
    manager_id = request.GET.get('manager_id')
    manager0 = Tbmanager.objects.get(manager_id=manager_id)
    manager = []
    dictionary = {}
    dictionary["manager_id"] = manager0.manager_id
    dictionary["name"] = manager0.name
    if manager0.sex is not None:
        dictionary["sex"] = manager0.sex
    else:
        dictionary["sex"] = ""
    dictionary["phonenumber"] = manager0.phonenumber
    if manager0.school is not None:
        dictionary["school"] = manager0.school
    else:
        dictionary["school"] = ""
    if manager0.e_mail is not None:
        dictionary["e_mail"] = manager0.e_mail
    else:
        dictionary["e_mail"] = ""
    manager.append(dictionary)
    return render(request, 'wechat/manager_infomation.html', {'manager': manager})
#管理员信息完善界面(提交按钮）
def manager_ifo_submit(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
    if request.method == "POST":
        manager_id = request.POST.get('manager_id')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        phonenumber = request.POST.get('phonenumber')
        school = request.POST.get('school')
        e_mail = request.POST.get('e_mail')
        Tbmanager.objects.filter(manager_id=manager_id).update(name= name,sex=sex,phonenumber=phonenumber,school=school,e_mail=e_mail)
        return HttpResponseRedirect('../manager_manage_list/')
    else:
        return HttpResponse("请求错误")
#评价管理
#校外兼职评价展示界面
def outwork_feedback(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
    list0 = Tbcompany.objects.all()
    out_feed = []
    for i in list0:
        dictionary1 = {}
        dictionary1["com_number"] = i.com_number
        dictionary1["com_name"] = i.com_name
        count = 0
        n=0
        feed_content = []
        worklist = TboutWork.objects.filter(com_number=i)
        for j in worklist:
            feedbackEr = TbfeedbackEr.objects.filter(ow_number=j).filter(fb_direction="学生评价企业")
            for k in feedbackEr:
                dictionary2 = {}
                dictionary2["nickname"] = k.stu.nickname
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
                count = count + int(fb_content[0])
                n=n+1
                dictionary2["fb_content2"] = content
                dictionary2["fb_time"] = k.fb_time.strftime("%Y-%m-%d, %H:%M:%S")
                feed_content.append(dictionary2)
        dictionary1["feed_content"] = feed_content
        if count !=0:
            f = count / n
            dictionary1["num"] = n
            dictionary1["fb_content1"] = '%.1f' % f
            out_feed.append(dictionary1)
    return render(request, 'wechat/outwork_feedback.html', {'out_feed': out_feed})
#校内兼职评价展示界面
def inwork_feedback(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
    list0 =["教务处","党政办","纪委办","资产处","志愿队","校工会","学工部","出国培训部","科研院","安保处","后勤部","学院","教师","其他"]
    in_feed = []
    number=3000000000
    for i in list0:
        dictionary1 = {}
        dictionary1["iw_depart"] = i
        count = 0
        n=0
        feed_content = []
        worklist = TbinWork.objects.filter(iw_depart=i)
        for j in worklist:
            feedbackEr = TbfeedbackEr.objects.filter(iw_number=j).filter(fb_direction="学生评价企业")
            for k in feedbackEr:
                dictionary2 = {}
                dictionary2["nickname"] = k.stu.nickname
                dictionary2["work"] = j.iw_post
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
                count = count + int(fb_content[0])
                n=n+1
                dictionary2["fb_content2"] = content
                dictionary2["fb_time"] = k.fb_time.strftime("%Y-%m-%d, %H:%M:%S")
                feed_content.append(dictionary2)
        dictionary1["feed_content"] = feed_content
        if count !=0:
            f = count / n
            number = number + 1
            dictionary1["number"] = number
            dictionary1["num"] = n
            dictionary1["fb_content1"] = '%.1f' % f
            in_feed.append(dictionary1)
    return render(request, 'wechat/inwork_feedback.html', {'in_feed': in_feed})
#学生评价展示界面
def stu_feedback_show(request):
    username = request.COOKIES.get('username', '')
    if not username:
        return HttpResponseRedirect('../login/')
    list0 = Tbstudent.objects.all()
    stu_feed = []
    for i in list0:
        dictionary1 = {}
        dictionary1["name"] = i.name
        dictionary1["stu_id"] = i.stu_id
        count = 0
        n=0
        feed_content = []
        feedbackEr = TbfeedbackEr.objects.filter(stu=i).filter(fb_direction="企业评价学生")
        for k in feedbackEr:
            if k.iw_number is not None:
                dictionary2 = {}
                dictionary2["css"] = "comment-type1"
                dictionary2["type"] = "校内"
                dictionary2["depart"] = k.iw_number.iw_depart
                dictionary2["work"] = k.iw_number.iw_post
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
                count = count + int(fb_content[0])
                n=n+1
                dictionary2["fb_content2"] = content
                dictionary2["fb_time"] = k.fb_time.strftime("%Y-%m-%d, %H:%M:%S")
                feed_content.append(dictionary2)
            else:
                dictionary2 = {}
                dictionary2["css"] = "comment-type2"
                dictionary2["type"] = "校外"
                dictionary2["depart"] = k.ow_number.com_number.com_name
                dictionary2["work"] = k.ow_number.ow_post
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
                count = count + int(fb_content[0])
                n = n + 1
                dictionary2["fb_content2"] = content
                dictionary2["fb_time"] = k.fb_time.strftime("%Y-%m-%d, %H:%M:%S")
                feed_content.append(dictionary2)
        dictionary1["feed_content"] = feed_content
        if count !=0:
            f = count / n
            dictionary1["num"] = n
            dictionary1["fb_content1"] = '%.1f' % f
            stu_feed.append(dictionary1)
    return render(request, 'wechat/stu_feedback_show.html', {'stu_feed': stu_feed})




