from django.shortcuts import HttpResponse,render
from django.template import loader
from .models import Tbcompany, Tbmanager, Tbstudent,Tbresume, Tbqualify,TbinWork,TboutWork,Tbapplication
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
import json
from itertools import chain
#小程序界面


def detail(request, manager_id):
    return HttpResponse("You're looking at managerid %s." % manager_id)


#login登录功能
@csrf_exempt
def dengluzhuce_login(request):
    if request.method == "POST":
        account_num = request.POST.get('no')
        passwd = request.POST.get('pwd')
        if len(account_num) == 8:
            try:
               user = Tbmanager.objects.get(manager_id=account_num)
               if user.password != passwd:
                    return HttpResponse("用户名或密码错误")
            except Tbmanager.DoesNotExist as e:
                return HttpResponse("用户名不存在")
        # 登录成功
            print(account_num)
            print(passwd)
            return HttpResponse("登录成功！")
        else:
            if len(account_num) == 11:
                try:
                    user = Tbcompany.objects.get(phone_num=account_num)
                    if user.password != passwd:
                        return HttpResponse("用户名或密码错误")
                except Tbcompany.DoesNotExist as e:
                    return HttpResponse("用户名不存在")
                # 登录成功
                print(account_num)
                print(passwd)
                return HttpResponse("登录成功！")
            else:
                if len(account_num) == 13:
                    try:
                        user = Tbstudent.objects.get(stu_id=account_num)
                        if user.password != passwd:
                            return HttpResponse("用户名或密码错误")
                    except Tbstudent.DoesNotExist as e:
                        return HttpResponse("用户名不存在")
                    # 登录成功
                    print(account_num)
                    print(passwd)
                    return HttpResponse("登录成功！")
                else:
                    return HttpResponse("用户名不存在")
    else:
        return HttpResponse("请求错误")

#regManager 注册功能
@csrf_exempt
def Manage_register(request):
    #curtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());注册时间？
    if request.method == "POST":
        account_num = request.POST.get('ManNumber')
        account_name = request.POST.get('Name')
        account_phone=request.POST.get('phoneNum')
        passwd_1 = request.POST.get('password')
        filterResult =Tbmanager.objects.filter(manager_id=account_num)
        if len(filterResult) > 0:
            return HttpResponse("用户已存在")
        else:
            user = Tbmanager.objects.create(manager_id=account_num, name=account_name, phonenumber=account_phone, password=passwd_1)
            user.save()
            return HttpResponse("注册成功")
    else:
        return HttpResponse("请求错误")

#regstudent 学生注册
@csrf_exempt
def Student_register(request):
    if request.method == "POST":
        account_num = request.POST.get('stuNumber')
        account_name = request.POST.get('Name')
        nickname = request.POST.get('NickName')
        account_phone=request.POST.get('phoneNum')
        passwd_1 = request.POST.get('password')

        filterResult =Tbstudent.objects.filter(stu_id=account_num)
        if len(filterResult) > 0:
            return HttpResponse("用户已存在")
        else:
            resume=Tbresume.objects.create(name=account_name)
            resume.save()
            user = Tbstudent.objects.create(stu_id=account_num, name=account_name, nickname=nickname, phonenumber_phonenumberphonenumber_phonenumber=account_phone, password=passwd_1, res_id=resume)
            user.save()
            return HttpResponse("注册成功")
    else:
        return HttpResponse("请求错误")

#regcompany 企业注册
@csrf_exempt
def Company_register(request):
    if request.method == "POST":
        account_name = request.POST.get('ComName')
        account_phone=request.POST.get('phoneNum')
        account_num =request.POST.get('ComLicense')
        passwd_1 = request.POST.get('password')
        filterResult1 = Tbcompany.objects.filter(com_license=account_num)
        filterResult2 = Tbcompany.objects.filter(phone_num=account_phone)
        if len(filterResult1) > 0:
            return HttpResponse("统一信用代码已注册")
        else:
            if len(filterResult2) > 0:
                return HttpResponse("电话号码已注册")
            else:
                user = Tbcompany.objects.create(com_license=account_num, com_name=account_name, phone_num=account_phone, password=passwd_1)
                user.save()
                qualify = Tbqualify.objects.create(com_license=account_num)
                qualify.save()
                return HttpResponse("注册成功")
    else:
        return HttpResponse("请求错误")

#repsw1 忘记密码验证身份页面
@csrf_exempt
def Reset_password_f1(request):
    if request.method == "POST":
        stu_id = request.POST.get('user')
        phonenumber = request.POST.get('phone')
        filterResult1 = Tbstudent.objects.filter(stu_id=stu_id)
        filterResult2 = Tbstudent.objects.filter(phonenumber_phonenumberphonenumber_phonenumber=phonenumber)
        if len(filterResult1) > 0 and len(filterResult2) > 0:
            return HttpResponse("身份验证成功")
        else:
            return HttpResponse("身份验证失败")
    else:
        return HttpResponse("请求错误")

#repsw1-1 忘记密码重置密码界面
@csrf_exempt
def Reset_password_f2(request):
    if request.method == "POST":
        stu_id = request.POST.get('user')
        new_password=request.POST.get('newpwd')
        Tbstudent.objects.filter(stu_id=stu_id ).update(password=new_password)
        return HttpResponse("密码修改成功")
    else:
        return HttpResponse("请求错误")

#以下是学生界面功能
#scenter返回学生名称
@csrf_exempt
def Show_student_name(request):
    if request.method == "POST":
        stu_id = request.POST.get('sno')  #前端从Get_outwork_info界面接收ow_number并存为全局变量
        user = Tbstudent.objects.get(stu_id=stu_id)
        name = user.name
        return HttpResponse(json.dumps({"name":name}))
    else:
        return HttpResponse("请求错误")

#sinfoShow 简历显示功能  #cresumeReview 企业端简历显示功能
@csrf_exempt
def Insert_resume_show(request):
    if request.method == "POST":
        stu_id = request.POST.get('stuNumber') # 唯一标识简历的全局变量
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
        return HttpResponse(json.dumps(
            {"name": name,
             "age": age,
             "sex": sex,
             "res_asses": res_asses,
             "res_edu": res_edu,
             "res_work": res_work,
             "res_proj": res_proj,
             "res_extra": res_extra,
             "res_per": res_per}))
    else:
        return HttpResponse("请求错误")

#Sinfofill 简历修改功能
@csrf_exempt
def Insert_resume_change(request):
    if request.method == "POST":
        stu_id = request.POST.get('stuNumber')  # 唯一标识简历的全局变量
        account_name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('gender')
        res_asses = request.POST.get('tech')
        res_edu = request.POST.get('edu')
        res_work = request.POST.get('job')
        res_proj = request.POST.get('project')
        res_extra = request.POST.get('practice')
        res_per = request.POST.get('works')
        user = Tbstudent.objects.get(stu_id=stu_id)
        res_id = user.res_id.res_id
        Tbresume.objects.filter(res_id=res_id).update(name=account_name, age=age, sex=sex, res_asses=res_asses, res_edu=res_edu, res_work=res_work, res_proj=res_proj, res_extra=res_extra, res_per=res_per)
        return HttpResponse("填写完成") #这里用filter get没有update
    else:
        return HttpResponse("请求错误")

#Sinfomodify 修改个人信息总界面
@csrf_exempt
def Reset_show(request):
    if request.method == "POST":
        stu_id = request.POST.get('stuNumber') # 唯一标识简历的全局变量
        user = Tbstudent.objects.get(stu_id=stu_id)
        name=user.name
        nickname=user.nickname
        phonenumber=user.phonenumber_phonenumberphonenumber_phonenumber
        e_mail=user.e_mail
        return HttpResponse(json.dumps(
            {"name":name ,
             "nickname": nickname,
             "phonenumber":phonenumber,
             "e_mail":e_mail}))
    else:
        return HttpResponse("请求错误")

#repwd2 修改密码
@csrf_exempt
def Reset_password(request):
    if request.method == "POST":
        stu_id = request.POST.get('no')
        origin_password=request.POST.get('oldpwd')
        new_password=request.POST.get('newpwd')

        filterResult1 = Tbstudent.objects.filter(password=origin_password)
        if len(filterResult1) > 0:
            Tbstudent.objects.filter(stu_id=stu_id ).update(password=new_password)
            return HttpResponse("密码修改成功")
        else:
            return HttpResponse("原密码输入不正确，请重新输入")
    else:
        return HttpResponse("请求错误")

#修改姓名 未调试
@csrf_exempt
def Reset_myinfo_name(request):
    if request.method == "POST":
        stu_id=request.POST.get('stuNumber')
        name=request.POST.get('name')
        Tbstudent.objects.filter(stu_id=stu_id ).update(name=name)
        return HttpResponse("姓名修改成功")
    else:
        return HttpResponse("请求错误")

#修改昵称 未调试
@csrf_exempt
def Reset_myinfo_nickname(request):
    if request.method == "POST":
        stu_id=request.POST.get('stuNumber')
        nickname=request.POST.get('nickName')
        Tbstudent.objects.filter(stu_id=stu_id ).update(nickname=nickname)
        return HttpResponse("昵称修改成功")
    else:
        return HttpResponse("请求错误")

#修改手机号码 未调试
@csrf_exempt
def Reset_myinfo_phonenumber(request):
    if request.method == "POST":
        stu_id=request.POST.get('stuNumber')
        phonenumber=request.POST.get('phoneNum')
        filterResult1 = Tbstudent.objects.filter(phonenumber_phonenumberphonenumber_phonenumber=phonenumber)
        if len(filterResult1) > 0:
            return HttpResponse("手机号码已注册")
        else:
            Tbstudent.objects.filter(stu_id=stu_id ).update(phonenumber_phonenumberphonenumber_phonenumber=phonenumber)
            return HttpResponse("电话号码修改成功")
    else:
        return HttpResponse("请求错误")

#修改邮箱 未调试
@csrf_exempt
def Reset_myinfo_e_mail(request):
    if request.method == "POST":
        stu_id=request.POST.get('sno')
        e_mail=request.POST.get('eMail')
        filterResult1 = Tbstudent.objects.filter(e_mail=e_mail)
        if len(filterResult1) > 0:
            return HttpResponse("邮箱已被占用")
        else:
            Tbstudent.objects.filter(stu_id=stu_id ).update(e_mail=e_mail)
            return HttpResponse("邮箱修改成功")
    else:
        return HttpResponse("请求错误")

#Salljob 校内外兼职信息展示界面
@csrf_exempt
def Show_work(request):
    result1 = TboutWork.objects.filter(ow_status='报名中')
    result2 = TbinWork.objects.filter(In_status='报名中')
    plays = []
    for i in result1:
            user = TboutWork.objects.get(ow_number=i.ow_number)
            com_number = user.com_number.com_number
            com_name = Tbcompany.objects.get(com_number=com_number).com_name
            plays.append({'type':'校外','title':i.ow_post,'amount':i.w_amount,'place':i.w_place,'salary':i.w_salary,'depart':com_name,'ow_number':i.ow_number})
    for i in result2:
        plays.append({'type':'校内','title':i.iw_post,'amount':i.w_amount,'place':i.w_place,'salary':i.w_salary,'depart':i.iw_depart,'iw_number':i.iw_number})
    plays_json = json.dumps(plays,ensure_ascii=False)
    return HttpResponse(plays_json)

#Salljob 校内兼职信息展示界面
# @csrf_exempt
# def Show_inwork(request):
#     result2 = TbinWork.objects.all().filter(In_status='报名中')
#     plays = []
#     for i in result2:
#         plays.append({'type':'校内','title':i.iw_post,'amount':i.w_amount,'place':i.w_place,'salary':i.w_salary,'depart':i.iw_depart,'iw_number':i.iw_number})
#     plays_json2 = json.dumps(plays,ensure_ascii=False)
#     return HttpResponse(plays_json2)

#Salljob 查询类型功能

#Salljob 查询距离功能

#Salljob 查询区域

#Sbaoming 兼职详情展示
@csrf_exempt
def Show_outwork_detail(request):
    if request.method == "POST":
        ow_number = request.POST.get('ow_number')
        result = TboutWork.objects.get(ow_number=ow_number)
        ow_post = result.ow_post
        w_time = result.w_time
        w_place_detail = result.w_place_detail
        w_salary = result.w_salary
        work = result.work
        w_reuire = result.w_reuire
        w_amount = result.w_amount
        ddl_time = str(result.ddl_time)
        w_ps = result.w_ps
        num = Tbapplication.objects.filter(ow_number=ow_number).count()
        return HttpResponse(json.dumps(
            {"post": ow_post,
             "time": w_time,
             "detail": w_place_detail,
             "salary": w_salary,
             "description": work,
             "ask": w_reuire,
             "num": w_amount,
             "ddl":ddl_time,
             "ps":w_ps,
             "already":num}))
    else:
        return HttpResponse("请求错误")

@csrf_exempt
def Show_inwork_detail(request):
    if request.method == "POST":
        iw_number = request.POST.get('iw_number')
        result = TbinWork.objects.get(iw_number=iw_number)
        iw_post = result.iw_post
        w_time = result.w_time
        w_place = result.w_place
        w_salary = result.w_salary
        work = result.work
        w_reuire = result.w_reuire
        w_amount = result.w_amount
        ddl_time = str(result.ddl_time)
        w_ps = result.w_ps
        num = Tbapplication.objects.filter(iw_number=iw_number).count()
        return HttpResponse(json.dumps(
            {"post": iw_post,
             "time": w_time,
             "detail": w_place,
             "salary": w_salary,
             "description": work,
             "ask": w_reuire,
             "num": w_amount,
             "ddl": ddl_time,
             "ps": w_ps,
             "already": num}))
    else:
        return HttpResponse("请求错误")

#Sreason 报名功能
@csrf_exempt
def Enroll_in_work(request):
    if request.method == "POST":
        stu = request.POST.get('user')
        ap_reson = request.POST.get('reason')
        get_ow_number = request.POST.get('ow_number')
        user = TboutWork.objects.get(ow_number=get_ow_number)
        student = Tbstudent.objects.get(stu_id=stu)
        application = Tbapplication.objects.create(ap_reson=ap_reson,ow_number=user,stu=student)
        application.save()
        return HttpResponse("报名成功")
    else:
        return HttpResponse("请求错误")

#Sbaoming 报名功能
@csrf_exempt
def Enroll_in_inwork(request):
    if request.method == "POST":
        stu = request.POST.get('user')
        get_iw_number = request.POST.get('iw_number')
        user = TbinWork.objects.get(iw_number=get_iw_number)
        student = Tbstudent.objects.get(stu_id=stu)
        application = Tbapplication.objects.create(iw_number=user,stu=student,In_status='已报名')
        application.save()
        return HttpResponse("报名成功")
    else:
        return HttpResponse("请求错误")

#smyjob 学生报名展示
@csrf_exempt
def Show_myjob(request):
    if request.method == "GET":
        stu = request.GET.get('user')
        application = Tbapplication.objects.filter(stu=stu)
        plays = []
        for item in application:
            apply_status = item.apply_status
            if item.iw_number is not None:
                iw_number = item.iw_number.iw_number
                result = TbinWork.objects.filter(iw_number=iw_number)
                for i in result:
                    plays.append({'type': '校内', 'title': i.iw_post, 'depart': i.iw_depart,'status': apply_status})
                plays_json = json.dumps(plays, ensure_ascii=False)
            else:
                result = TboutWork.objects.filter(ow_number=item.ow_number.ow_number)
                for i in result:
                    user = TboutWork.objects.get(ow_number=i.ow_number)
                    com_number = user.com_number.com_number
                    com_name = Tbcompany.objects.get(com_number=com_number).com_name
                    plays.append({'type': '校外', 'title': i.ow_post, 'depart': com_name,'status': apply_status})
                plays_json = json.dumps(plays, ensure_ascii=False)
        return HttpResponse(plays_json)
    else:
        return HttpResponse("请求错误")




