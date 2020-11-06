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
        resume= Tbresume.objects.get(res_id = res_id)
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

#简历修改功能 #改到这里了和前端还未调试
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

#企业信息修改？（未写）

#企业兼职信息发布功能 对应cjobrelease界面
@csrf_exempt
def Part_time_post(request):
    if request.method == "POST":
        phone_num = request.POST.get('') #前端加全局变量，企业的注册手机号，改数据库
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

        filterResult1 = Tbcompany.objects.filter(phone_num=phone_num)
        if len(filterResult1) > 0:
            com_number = filterResult1.com_number
            outwork = TboutWork.objects.create(ow_post=ow_post,w_time=w_time,w_place=w_place,work=work,w_salary=w_salary,w_reuire=w_reuire,w_amount=w_amount,ddl_time=ddl_time,inpub_time=inpub_time,w_ps=w_ps,com_number=com_number,ow_status = 'waiting')
            outwork.save()
            return HttpResponse("发布成功")
        else:
            return HttpResponse("请求错误")

#企业兼职信息展示功能
@csrf_exempt
def Get_outwork_info(request):
    if request.method == "POST":
        com_license = request.POST.getlist('XXXX')#传的是企业工商号？
        filterResult1 = Tbcompany.objects.filter(com_license=com_license)
        if len(filterResult1) > 0:
            com_number = filterResult1.objects.values("com_number").first()
            outwork_info = TboutWork.objects.get(com_number=com_number) #只返回这些数据的某些列，需要根据页面显示调整
            return HttpResponse &outwork_info
        else:
            return HttpResponse("请求错误")

#企业“单条”兼职信息展示功能
@csrf_exempt
def Get_outwork_detail_info(request):
    if request.method == "POST":
        com_license = request.POST.getlist('XXXX')#传的是企业工商号？
        ow_number = request.POST.get('XXXXX')  # 这里工作号是数据库自动生成的，不知道怎么从前端传给后端，建议是工作考是不是可以考虑微信那边生成，然后传给数据库保存
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
        com_license = request.POST.getlist('XXXX')
        ow_number = request.POST.get('XXXXX') #这里工作号是数据库自动生成的，不知道怎么从前端传给后端
        ow_post = request.POST.getlist('') #这个值应该可以不用传，因为岗位应该不允许修改
        w_time = request.POST.getlist('')
        w_place = request.POST.getlist('')
        work = request.POST.getlist('')
        w_salary = request.POST.getlist('')
        w_reuire = request.POST.getlist('')
        w_amount = request.POST.getlist('')
        ddl_time = request.POST.getlist('')
        ipub_time = request.POST.getlist('')
        w_ps = request.POST.getlist('')

        TboutWork.objects.filter(ow_number=ow_number ).update(w_time=w_time, w_place=w_place, work=work, w_salary=w_salary, w_reuire=w_reuire, w_amount=w_amount, ddl_time=ddl_time, ipub_time=ipub_time, w_ps=w_ps)
        return HttpResponse("修改成功")
    else:
        return HttpResponse("请求错误")

@csrf_exempt
def Part_time_post(request):
    if request.method == "POST":
        ow_number = request.POST.getlist('') #不确定这个传不传，前端知道？
        ow_post = request.POST.getlist('')
        w_time = request.POST.getlist('')
        w_place = request.POST.getlist('')
        work  = request.POST.getlist('')
        w_salary = request.POST.getlist('')
        w_reuire = request.POST.getlist('')
        w_amount = request.POST.getlist('')
        ddl_time = request.POST.getlist('')
        ipub_time = request.POST.getlist('')
        w_ps = request.POST.getlist('')
        com_license = request.POST.getlist('')#传的是企业工商号？

        filterResult1 = Tbcompany.objects.filter(com_license=com_license)
        if len(filterResult1) > 0:
            com_number = filterResult1.objects.values("com_number").first()
            TboutWork.objects.get(com_number=com_number).update(ow_status = 'waiting', )#1.不认识TboutWork？2.后面加传过来的值并更新
            return HttpResponse("发布成功")
        else:
            return HttpResponse("请求错误")

@csrf_exempt
def Get_outwork_info(request):
    if request.method == "POST":
        com_license = request.POST.getlist('XXXX')#传的是企业工商号？
        filterResult1 = Tbcompany.objects.filter(com_license=com_license)
        if len(filterResult1) > 0:
            com_number = filterResult1.objects.values("com_number").first()
            outwork_info = TboutWork.objects.get(com_number=com_number) #只返回这些数据的某些列，需要根据页面显示调整
            return HttpResponse &outwork_info
        else:
            return HttpResponse("请求错误")

@csrf_exempt
def Get_outwork_detail_info(request):
    if request.method == "POST":
        com_license = request.POST.getlist('XXXX')#传的是企业工商号？
        ow_number = request.POST.get('XXXXX')  # 这里工作号是数据库自动生成的，不知道怎么从前端传给后端，建议是工作考是不是可以考虑微信那边生成，然后传给数据库保存
        filterResult1 = TboutWork.objects.filter(ow_number=ow_number)
        if len(filterResult1) > 0:
            outwork_detail_info = TboutWork.objects.get(ow_number=ow_number)
            return HttpResponse &outwork_detail_info
        else:
            return HttpResponse("请求错误")

@csrf_exempt
def Modify_outwork_info(request):
    if request.method == "POST":
        com_license = request.POST.getlist('XXXX')
        ow_number = request.POST.get('XXXXX') #这里工作号是数据库自动生成的，不知道怎么从前端传给后端
        ow_post = request.POST.getlist('') #这个值应该可以不用传，因为岗位应该不允许修改
        w_time = request.POST.getlist('')
        w_place = request.POST.getlist('')
        work = request.POST.getlist('')
        w_salary = request.POST.getlist('')
        w_reuire = request.POST.getlist('')
        w_amount = request.POST.getlist('')
        ddl_time = request.POST.getlist('')
        ipub_time = request.POST.getlist('')
        w_ps = request.POST.getlist('')

        TboutWork.objects.get(ow_number=ow_number ).update(w_time=w_time, w_place=w_place, work=work, w_salary=w_salary, w_reuire=w_reuire, w_amount=w_amount, ddl_time=ddl_time, ipub_time=ipub_time, w_ps=w_ps)
        return HttpResponse("修改成功")
    else:
        return HttpResponse("请求错误")

@csrf_exempt
def Stop_outwork(request):
    if request.method == "POST":
        ow_number = request.POST.get('XXXXX')
        filterResult1 = TboutWork.objects.filter(ow_number=ow_number)
        if len(filterResult1) > 0:
            TboutWork.objects.get(ow_number=ow_number ).update(ow_status = 'stop')
            return HttpResponse("该招聘已停止")
        else:
            return HttpResponse("请求错误")

#企业兼职信息状态修改界面
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



