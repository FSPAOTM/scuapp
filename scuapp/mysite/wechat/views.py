from django.shortcuts import HttpResponse,render
from django.template import loader
from .models import Tbcompany, Tbmanager, Tbstudent,Tbresume, Tbqualify,TbinWork,TboutWork
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
import json
#小程序界面


def detail(request, manager_id):
    return HttpResponse("You're looking at managerid %s." % manager_id)


#登录功能  login界面
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

#注册功能
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

#简历显示功能
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

#简历修改功能
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

#修改个人信息总界面
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

#修改密码
@csrf_exempt
def Reset_password(request):
    if request.method == "POST":
        stu_id = request.POST.get('stuNumber')
        origin_password=request.POST.get('js传数据的原密码')
        new_password=request.POST.get('js传数据的新密码')

        filterResult1 = Tbstudent.objects.filter(password=origin_password)
        if len(filterResult1) > 0:
            Tbstudent.objects.filter(stu_id=stu_id ).update(password=new_password)
            return HttpResponse("密码修改成功")
        else:
            return HttpResponse("原密码输入不正确，请重新输入")
    else:
        return HttpResponse("请求错误")

#忘记密码验证身份页面
@csrf_exempt
def Reset_password_f1(request):
    if request.method == "POST":
        stu_id = request.POST.get('user')
        phonenumber = request.POST.get('phone')
        filterResult1 = Tbstudent.objects.filter(stu_id=stu_id)
        filterResult2 = Tbstudent.objects.filter(phonenumber=phonenumber)
        if len(filterResult1) > 0 and len(filterResult2) > 0:
            return HttpResponse("身份验证成功")
        else:
            return HttpResponse("身份验证失败")
    else:
        return HttpResponse("请求错误")

#忘记密码重置密码界面
@csrf_exempt
def Reset_password_f2(request):
    if request.method == "POST":
        stu_id = request.POST.get('user')
        new_password=request.POST.get('newpwd')
        Tbstudent.objects.filter(stu_id=stu_id ).update(password=new_password)
        return HttpResponse("密码修改成功")
    else:
        return HttpResponse("请求错误")

#修改姓名
@csrf_exempt
def Reset_myinfo_name(request):
    if request.method == "POST":
        stu_id=request.POST.get('stuNumber')
        name=request.POST.get('name')
        Tbstudent.objects.filter(stu_id=stu_id ).update(name=name)
        return HttpResponse("姓名修改成功")
    else:
        return HttpResponse("请求错误")

#修改昵称
@csrf_exempt
def Reset_myinfo_nickname(request):
    if request.method == "POST":
        stu_id=request.POST.get('stuNumber')
        nickname=request.POST.get('nickName')
        Tbstudent.objects.filter(stu_id=stu_id ).update(nickname=nickname)
        return HttpResponse("昵称修改成功")
    else:
        return HttpResponse("请求错误")

#修改手机号码
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

#修改邮箱
@csrf_exempt
def Reset_myinfo_e_mail(request):
    if request.method == "POST":
        stu_id=request.POST.get('stuNumber')
        e_mail=request.POST.get('eMail')
        filterResult1 = Tbstudent.objects.filter(e_mail=e_mail)
        if len(filterResult1) > 0:
            return HttpResponse("邮箱已被占用")
        else:
            Tbstudent.objects.filter(stu_id=stu_id ).update(e_mail=e_mail)
            return HttpResponse("邮箱修改成功")
    else:
        return HttpResponse("请求错误")

#企业信息修改显示功能
@csrf_exempt
def Company_info_showmodiify(request):
    if request.method == "POST":
        phone_num = request.POST.get('phone')  # 唯一标识简历的全局变量
        user = Tbcompany.objects.get(phone_num=phone_num)
        com_License = user.com_License
        com_name = user.com_name
        com_leader = user.com_leader
        e_mail = user.e_mail
        com_address = user.com_address
        qualify = Tbqualify.objects.get(com_License=com_License)
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

#企业信息修改功能
@csrf_exempt
def Company_info_modiify(request):
    if request.method == "POST":
        com_License = request.POST.get('cno')  # 唯一标识简历的全局变量
        phone_num = request.POST.get('phone')
        com_leader = request.POST.get('manname')
        e_mail = request.POST.get('email')
        com_address = request.POST.get('address')
        com_business = request.POST.get('contents')
        com_status = request.POST.get('condition')
        Tbcompany.objects.filter(com_License=com_License).update(phone_num=phone_num, com_leader=com_leader, e_mail=e_mail, com_address=com_address)
        Tbqualify.objects.filter(com_License=com_License).update(com_business=com_business, com_status=com_status)
        return HttpResponse("填写完成") #这里用filter get没有update
    else:
        return HttpResponse("请求错误")

#企业兼职信息发布功能 对应cjobrelease界面
@csrf_exempt
def Part_time_post(request):
    if request.method == "POST":
        phone_num = request.POST.get('')
        ow_post = request.POST.get('Name')
        w_time = request.POST.get('jobtime')
        w_place = request.POST.get('location')
        work = request.POST.get('description')
        w_salary = request.POST.get('salary')
        w_reuire = request.POST.get('ask')
        w_amount = request.POST.get('num')
        ddl_time = request.POST.get('endingtim')
        inpub_time = timezone.now()
        w_ps = request.POST.getlist('ps')

        User = Tbcompany.objects.get(phone_num=phone_num)
        com_number = User.com_number
        outwork = TboutWork.objects.create(ow_post=ow_post,w_time=w_time,w_place=w_place,work=work,w_salary=w_salary,w_reuire=w_reuire,w_amount=w_amount,ddl_time=ddl_time,inpub_time=inpub_time,w_ps=w_ps,com_number=com_number,ow_status = 'waiting')
        outwork.save()
        return HttpResponse("发布成功")
    else:
        return HttpResponse("请求错误")

#企业兼职信息展示功能
@csrf_exempt
def Get_outwork_info(request):
    if request.method == "POST":
        phone_num = request.POST.get('')
        User = Tbcompany.objects.get(phone_num=phone_num)
        com_number = User.com_number
        outwork_info = TboutWork.objects.get(com_number=com_number) #只返回这些数据的某些列，需要根据页面显示调整
        return HttpResponse &outwork_info #这里要是传不了就改成前面的原始方法
    else:
        return HttpResponse("请求错误")

#企业“单条”兼职信息展示功能
@csrf_exempt
def Get_outwork_detail_info(request):
    if request.method == "POST":
        ow_number = request.POST.get('XXXXX')  #前端从Get_outwork_info界面接收ow_number并存为全局变量
        filterResult1 = TboutWork.objects.filter(ow_number=ow_number)
        if len(filterResult1) > 0:
            outwork_detail_info = TboutWork.objects.get(ow_number=ow_number)
            return HttpResponse &outwork_detail_info
        else:
            return HttpResponse("请求错误")

#企业兼职信息修改界面
@csrf_exempt
def Modify_outwork_info(request):
    if request.method == "POST":
        ow_number = request.POST.get('')
        ow_post = request.POST.get('Name') #前端提示岗位不可修改
        w_time = request.POST.get('jobtime')
        w_place = request.POST.get('location')
        work = request.POST.get('description')
        w_salary = request.POST.get('salary')
        w_reuire = request.POST.get('ask')
        w_amount = request.POST.get('num')
        ddl_time = request.POST.get('endingtim')
        inpub_time = timezone.now()
        w_ps = request.POST.getlist('ps')

        TboutWork.objects.filter(ow_number=ow_number).update(w_time=w_time, w_place=w_place, work=work, w_salary=w_salary, w_reuire=w_reuire, w_amount=w_amount, ddl_time=ddl_time, ipub_time=inpub_time, w_ps=w_ps)
        return HttpResponse("修改成功")
    else:
        return HttpResponse("请求错误")

#企业兼职信息状态修改界面 这个还没有加URL界面
@csrf_exempt
def Stop_outwork(request):
    if request.method == "POST":
        ow_number = request.POST.get('XXXXX')
        filterResult1 = TboutWork.objects.filter(ow_number=ow_number)
        if len(filterResult1) > 0:
            TboutWork.objects.filter(ow_number=ow_number ).update(ow_status = 'stop')
            return HttpResponse("该招聘已停止")
        else:
            return HttpResponse("请求错误")

#学生浏览所有兼职信息页面
@csrf_exempt
def Sget_outwork_info(request):
    if request.method == "POST":
        outwork_info = TboutWork.objects.get() #选择所有界面
        return HttpResponse &outwork_info #这里要是传不了就改成前面的原始方法
    else:
        return HttpResponse("请求错误")

#企业“单条”兼职信息展示功能
@csrf_exempt
def Sget_outwork_detail_info(request):
    if request.method == "POST":
        ow_number = request.POST.get('XXXXX')  #前端从Get_outwork_info界面接收ow_number并存为全局变量
        filterResult1 = TboutWork.objects.filter(ow_number=ow_number)
        if len(filterResult1) > 0:
            outwork_detail_info = TboutWork.objects.get(ow_number=ow_number)
            return HttpResponse &outwork_detail_info
        else:
            return HttpResponse("请求错误")



