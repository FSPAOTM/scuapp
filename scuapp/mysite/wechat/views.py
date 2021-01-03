from django.shortcuts import HttpResponse
from .models import Tbcompany, Tbmanager, Tbstudent,Tbresume, Tbqualify,TbinWork,TboutWork,Tbapplication,student
from django.utils import timezone
import json
from threading import Timer

#####报名结束状态生成（定时器自动更新）(时间是否需要修改）
def info_status():
    inlist = TbinWork.objects.filter(In_status='报名中')
    for i in inlist:
        iddl = (i.ddl_time - timezone.now()).days
        inow = Tbapplication.objects.filter(iw_number=i.iw_number).count()
        if iddl < 0 or inow >= int(i.w_amount):
            TbinWork.objects.filter(iw_number=i.iw_number).update(In_status='报名结束')
    outlist = TboutWork.objects.filter(ow_status="报名中")
    for j in outlist:
        oddl = (j.ddl_time - timezone.now()).days
        if oddl < 0:
            TboutWork.objects.filter(ow_number=j.ow_number).update(ow_status="报名结束")
    t = Timer(10, info_status, ())
    t.start()

info_status()

#小程序界面

#login登录功能
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
def Company_register(request):
    if request.method == "POST":
        account_name = request.POST.get('ComName')
        account_phone=request.POST.get('phoneNum')
        account_num =request.POST.get('ComLicense')
        passwd_1 = request.POST.get('password')
        filterResult1 = Tbqualify.objects.filter(com_license=account_num)
        filterResult2 = Tbcompany.objects.filter(phone_num=account_phone)
        if len(filterResult1) > 0:
            return HttpResponse("统一信用代码已注册")
        else:
            if len(filterResult2) > 0:
                return HttpResponse("电话号码已注册")
            else:
                qualify = Tbqualify.objects.create(com_license=account_num)
                qualify.save()
                user = Tbcompany.objects.create(com_license=qualify, com_name=account_name, phone_num=account_phone,
                                                password=passwd_1)
                user.save()
                return HttpResponse("注册成功")
    else:
        return HttpResponse("请求错误")

#repsw1 忘记密码验证身份页面
def Reset_password_f1(request):
    if request.method == "POST":
        id = request.POST.get('user')
        phonenumber = request.POST.get('phone')
        if len(id) == 13:
            filterResult1 = Tbstudent.objects.filter(stu_id=id).filter(phonenumber_phonenumberphonenumber_phonenumber=phonenumber)
            if len(filterResult1) > 0:
                return HttpResponse("身份验证成功")
            else:
                return HttpResponse("身份验证失败")
        else:
            if len(id) == 18:
                qualify = Tbqualify.objects.get(com_license=id)
                filterResult1 = Tbcompany.objects.filter(com_License=qualify).filter(phone_num=phonenumber)
                if len(filterResult1) > 0:
                    return HttpResponse("身份验证成功")
                else:
                    return HttpResponse("身份验证失败")
            else:
                return HttpResponse("用户不存在")
    else:
        return HttpResponse("请求错误")

#repsw1-1 忘记密码重置密码界面
def Reset_password_f2(request):
    if request.method == "POST":
        id = request.POST.get('user')
        new_password=request.POST.get('newpwd')
        if len(id) == 13:
            Tbstudent.objects.filter(stu_id=id ).update(password=new_password)
            return HttpResponse("密码修改成功")
        else:
            if len(id) == 11:
                Tbcompany.objects.filter(phone_num=id).update(password=new_password)
                return HttpResponse("密码修改成功")
    else:
        return HttpResponse("请求错误")

#以下是学生界面功能
#scenter返回学生名称
def Show_student_name(request):
    if request.method == "POST":
        stu_id = request.POST.get('sno')  #前端从Get_outwork_info界面接收ow_number并存为全局变量
        user = Tbstudent.objects.get(stu_id=stu_id)
        name = user.name
        return HttpResponse(json.dumps({"name":name}))
    else:
        return HttpResponse("请求错误")

#sinfoShow 学生端 简历显示功能
def Insert_resume_show(request):
    if request.method == "POST":
        stu_id = request.POST.get('stuNumber') # 唯一标识简历的全局变量
        user = Tbstudent.objects.get(stu_id=stu_id)
        res_id = user.res_id.res_id
        resume= Tbresume.objects.get(res_id=res_id)
        name=resume.name
        if resume.age is not None:
            age = resume.age
        else:
            age = ""
        if resume.sex is not None:
            sex = resume.sex
        else:
            sex = ""
        if resume.res_asses is not None:
            res_asses = resume.res_asses
        else:
            res_asses = ""
        if resume.res_edu is not None:
            res_edu = resume.res_edu
        else:
            res_edu = ""
        if resume.res_work is not None:
            res_work = resume.res_work
        else:
            res_work = ""
        if resume.res_proj is not None:
            res_proj = resume.res_proj
        else:
            res_proj = ""
        if resume.res_extra is not None:
            res_extra = resume.res_extra
        else:
            res_extra = ""
        if resume.res_per is not None:
            res_per = resume.res_per
        else:
            res_per = ""
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
def Reset_show(request):
    if request.method == "POST":
        stu_id = request.POST.get('stuNumber') # 唯一标识简历的全局变量
        user = Tbstudent.objects.get(stu_id=stu_id)
        name=user.name
        nickname=user.nickname
        phonenumber=user.phonenumber_phonenumberphonenumber_phonenumber
        if user.e_mail is not None:
            e_mail=user.e_mail
        else:
            e_mail = ""
        return HttpResponse(json.dumps(
            {"name":name ,
             "nickname": nickname,
             "phonenumber":phonenumber,
             "e_mail":e_mail}))
    else:
        return HttpResponse("请求错误")

#repwd2 修改密码
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

#修改姓名
def Reset_myinfo_name(request):
    if request.method == "POST":
        stu_id=request.POST.get('stuNumber')
        name=request.POST.get('name')
        Tbstudent.objects.filter(stu_id=stu_id ).update(name=name)
        return HttpResponse("姓名修改成功")
    else:
        return HttpResponse("请求错误")

#修改昵称
def Reset_myinfo_nickname(request):
    if request.method == "POST":
        stu_id=request.POST.get('stuNumber')
        nickname=request.POST.get('nickName')
        Tbstudent.objects.filter(stu_id=stu_id ).update(nickname=nickname)
        return HttpResponse("昵称修改成功")
    else:
        return HttpResponse("请求错误")

#修改手机号码
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
def Show_work(request):
    result1 = TboutWork.objects.filter(ow_status='报名中')
    result2 = TbinWork.objects.filter(In_status='报名中')
    plays = []
    for i in result1:
            user = TboutWork.objects.get(ow_number=i.ow_number)
            com_number = user.com_number.com_number
            com_name = Tbcompany.objects.get(com_number=com_number).com_name
            plays.append({'type':'校外','title':i.ow_post,'amount':i.w_amount,'place':i.w_place,'salary':i.w_salary,'depart':com_name,'iw_number':'NULL','ow_number':i.ow_number})
    for i in result2:
        plays.append({'type':'校内','title':i.iw_post,'amount':i.w_amount,'place':i.w_place,'salary':i.w_salary,'depart':i.iw_depart,'iw_number':i.iw_number})
    plays_json = json.dumps(plays,ensure_ascii=False)
    return HttpResponse(plays_json)

#Salljob 查询类型功能

#Salljob 查询距离功能

#Salljob 查询区域

#Sbaoming 兼职详情展示
def Show_outwork_detail(request):
    if request.method == "POST":
        ow_number = request.POST.get('ow_number')
        result = TboutWork.objects.get(ow_number=ow_number)
        ow_post = result.ow_post
        w_time = result.w_time
        w_place = result.w_place
        w_place_detail = result.w_place_detail
        w_salary = result.w_salary
        work = result.work
        w_reuire = result.w_reuire
        w_amount = result.w_amount
        ddl_time = result.ddl_time.strftime("%Y-%m-%d, %H:%M:%S")
        w_ps = result.w_ps
        num = Tbapplication.objects.filter(ow_number=ow_number).count()
        return HttpResponse(json.dumps(
            {"post": ow_post,
             "time": w_time,
             "location":w_place,
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
        ddl_time = result.ddl_time.strftime("%Y-%m-%d, %H:%M:%S")
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
def Enroll_in_work(request):
    if request.method == "POST":
        stu = request.POST.get('user')
        ap_reson = request.POST.get('reason')
        get_ow_number = request.POST.get('ow_number')
        user = TboutWork.objects.get(ow_number=get_ow_number)
        student = Tbstudent.objects.get(stu_id=stu)
        filterResult1 = Tbapplication.objects.filter(stu=stu,ow_number=get_ow_number)
        if len(filterResult1) > 0:
            return HttpResponse("该学生已报名")
        else:
            application = Tbapplication.objects.create(ap_reson=ap_reson,ap_time=timezone.now(),ow_number=user,stu=student)
            application.save()
            return HttpResponse("报名成功")
    else:
        return HttpResponse("请求错误")

#Sbaoming 报名功能
def Enroll_in_inwork(request):
    if request.method == "POST":
        stu = request.POST.get('user')
        get_iw_number = request.POST.get('iw_number')
        user = TbinWork.objects.get(iw_number=get_iw_number)
        student = Tbstudent.objects.get(stu_id=stu)
        filterResult1 = Tbapplication.objects.filter(stu=stu, iw_number=get_iw_number)
        if len(filterResult1) > 0:
            return HttpResponse("该学生已报名")
        else:
            application = Tbapplication.objects.create(iw_number=user,stu=student,apply_status='已报名',ap_time=timezone.now())
            application.save()
            return HttpResponse("报名成功")
    else:
        return HttpResponse("请求错误")

#smyjob 学生报名展示
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
                    if apply_status == "已评价":
                        plays.append({'type': '校内', 'title': i.iw_post, 'depart': i.iw_depart, 'status': apply_status,
                                  'place': i.w_place, 'salary': i.w_salary, 'iw_number': i.iw_number, 'show': False})
                    else:
                        plays.append({'type': '校内', 'title': i.iw_post, 'depart': i.iw_depart, 'status': apply_status,
                                  'place': i.w_place, 'salary': i.w_salary, 'iw_number': i.iw_number, 'show': True})
                plays_json = json.dumps(plays, ensure_ascii=False)
            else:
                result = TboutWork.objects.filter(ow_number=item.ow_number.ow_number)
                for i in result:
                    user = TboutWork.objects.get(ow_number=i.ow_number)
                    com_number = user.com_number.com_number
                    com_name = Tbcompany.objects.get(com_number=com_number).com_name
                    if apply_status == "已评价":
                        plays.append({'type': '校外', 'title': i.ow_post, 'depart': com_name, 'status': apply_status,
                                      'place': i.w_place, 'salary': i.w_salary, 'iw_number': "NULL",
                                      'ow_number': i.ow_number, 'show': False})
                    else:
                        plays.append({'type': '校外', 'title': i.ow_post, 'depart': com_name, 'status': apply_status,
                                      'place': i.w_place, 'salary': i.w_salary, 'iw_number': "NULL",
                                      'ow_number': i.ow_number, 'show': True})
                plays_json = json.dumps(plays, ensure_ascii=False)
        return HttpResponse(plays_json)
    else:
        return HttpResponse("请求错误")

#test
def test(request):
    result1 = student.objects.all()
    plays = []
    for i in result1:
        plays.append({'type': '校外', 'title': i.stu_id})
    plays_json = json.dumps(plays, ensure_ascii=False)
    return HttpResponse(plays_json)











