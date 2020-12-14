from django.shortcuts import HttpResponse,render
from django.template import loader
from .models import Tbcompany, Tbmanager, Tbstudent,Tbresume, Tbqualify,TbinWork,TboutWork,Tbapplication,TbinterviewNotice,TbfeedbackEr
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
import json
from itertools import chain
from . import views01
#小程序界面

#stongzhi 面试通知展示 TbinterviewNotice数据表 未加url未调试
def Interview_notice(request):
    if request.method == "GET":
        stu = request.GET.get('user')
        plays = []
        result = TbinterviewNotice.objects.filter(stu=stu)
        for i in result:
            plays.append({'address':i.i_address,'time':i.i_time,'number':i.i_number})
        plays_json = json.dumps(plays, ensure_ascii=False)
        return HttpResponse(plays_json)
    else:
        return HttpResponse("请求错误")

#stongzhi 学生接收面试通知 未加url未调试
def Interview_notice(request):
    if request.method == "GET":
        i_number = request.GET.get('i_number') #与改状态函数相关！！
        filterResult1 = TbinterviewNotice.objects.get(i_number=i_number)
        if len(filterResult1) > 0:
            filterResult1.update(s_sure='已确认')  #需要在数组内操作，待修改
            return HttpResponse("请求成功")
        else:
            return HttpResponse("请求错误")
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