from django.urls import path

from . import views,views01,views_com

app_name = 'wechat'
urlpatterns = [
    #小程序界面
    path('detail/<manager_id>/', views.detail, name='detail'),
    path('dengluzhuce_login/', views.dengluzhuce_login, name='dengluzhuce_login'),
    path('Manage_register/', views.Manage_register, name='Manage_register'),
    path('Student_register/', views.Student_register, name='Student_register'),
    path('Company_register/', views.Company_register, name='Company_register'),
    path('Show_student_name/', views.Show_student_name, name='Show_student_name'),
    path('Insert_resume_show/', views.Insert_resume_show, name='Insert_resume_show'),
    path('Insert_resume_change/', views.Insert_resume_change, name='Insert_resume_change'),
    path('Reset_show/', views.Reset_show, name='Reset_show'),
    path('Reset_password/', views.Reset_password, name='Reset_password'),
    path('Reset_password_f1/', views.Reset_password_f1, name='Reset_password_f1'),
    path('Reset_password_f2/', views.Reset_password_f2, name='Reset_password_f2'),
    path('Reset_myinfo_name/', views.Reset_myinfo_name, name='Reset_myinfo_name'),
    path('Reset_myinfo_nickname/', views.Reset_myinfo_nickname, name='Reset_myinfo_nickname'),
    path('Reset_myinfo_phonenumber/', views.Reset_myinfo_phonenumber, name='Reset_myinfo_phonenumber'),
    path('Reset_myinfo_e_mail/', views.Reset_myinfo_e_mail, name='Reset_myinfo_e_mail'),
    path('Show_work/', views.Show_work, name='Show_work'),
    path('Show_outwork_detail/', views.Show_outwork_detail, name='Show_outwork_detail'),
    path('Show_inwork_detail/', views.Show_inwork_detail, name='Show_inwork_detail'),
    path('Enroll_in_work/', views.Enroll_in_work, name='Enroll_in_work'),
    path('Enroll_in_inwork/', views.Enroll_in_inwork, name='Enroll_in_inwork'),
    path('Show_myjob/', views.Show_myjob, name='Show_myjob'),
    #企业
    path('Show_company_name/', views_com.Show_company_name, name='Show_company_name'),
    path('Company_info_showmodiify/', views_com.Company_info_showmodiify, name='Company_info_showmodiify'),
    path('Company_info_modiify/', views_com.Company_info_modiify, name='Company_info_modiify'),
    path('Part_time_post/', views_com.Part_time_post, name='Part_time_post'),
    path('Get_outwork_info/', views_com.Get_outwork_info, name='Get_outwork_info'),
    path('Get_outwork_detail_info/', views_com.Get_outwork_detail_info, name='Get_outwork_detail_info'),
    path('Modify_outwork_info/', views_com.Modify_outwork_info, name='Modify_outwork_info'),
    path('Show_applicant/', views_com.Show_applicant, name='Show_applicant'),
    path('Modify_applystatus/', views_com.Modify_applystatus, name='Modify_applystatus'),
    path('Company_apply_interviewtime/', views_com.Company_apply_interviewtime, name='Company_apply_interviewtime'),

    #后台管理界面
    #登录注册等
    path('', views01.index, name='index'),
    path('index/', views01.index, name='index'),
    path('manage/', views01.manage, name='manage'),
    path('login/', views01.login, name='login'),
    path('register/', views01.register, name='register'),
    path('inwork_foregetpwd/', views01.inwork_foregetpwd, name='inwork_foregetpwd'),
    path('management_login/', views01.management_login, name='management_login'),
    path('management_inwork_register/', views01.management_inwork_register, name='management_inwork_register'),
    path('management_forgetpwd/', views01.management_forgetpwd, name='management_forgetpwd'),
    #兼职管理
    path('inwork_list/', views01.inwork_list, name='inwork_list'),
    path('outwork_list/', views01.outwork_list, name='outwork_list'),
    path('inwork_add/', views01.inwork_add, name='inwork_add'),
    path('outwork_add/', views01.outwork_add, name='outwork_add'),
    path('management_inWork_stop/', views01.management_inWork_stop, name='management_inWork_stop'),
    path('management_inWork_release/', views01.management_inWork_release, name='management_inWork_release'),
    path('management_inWork_begin/', views01.management_inWork_begin, name='management_inWork_begin'),
    path('management_inWork_reset_show/', views01.management_inWork_reset_show, name='management_inWork_reset_show'),
    path('management_inWork_reset/', views01.management_inWork_reset, name='management_inWork_reset'),
    path('management_inWork_delete/', views01.management_inWork_delete, name='management_inWork_delete'),
    path('management_inwork_search/', views01.management_inwork_search, name='management_inwork_search'),
    path('management_outWork_stop/', views01.management_outWork_stop, name='management_outWork_stop'),
    path('management_outWork_release/', views01.management_outWork_release, name='management_outWork_release'),
    path('management_outWork_begin/', views01.management_outWork_begin, name='management_outWork_begin'),
    path('management_outWork_reset_show/', views01.management_outWork_reset_show, name='management_outWork_reset_show'),
    path('management_outWork_reset/', views01.management_outWork_reset, name='management_outWork_reset'),
    path('management_outWork_delete/', views01.management_outWork_delete, name='management_outWork_delete'),
    path('management_outwork_search/', views01.management_outwork_search, name='management_outwork_search'),
    #信息处理
    path('inworking_list/', views01.inworking_list, name='inworking_list'),
    path('inwork_stu_ifo/', views01.inwork_stu_ifo, name='inwork_stu_ifo'),
    path('management_inworking_search/', views01.management_inworking_search, name='management_inworking_search'),
    path('management_inWork_result/', views01.management_inWork_result, name='management_inWork_result'),
    path('inwork_result/', views01.inwork_result, name='inwork_result'),
    path('inwork_result_submit/', views01.inwork_result_submit, name='inwork_result_submit'),
    path('management_inWork_result_change/', views01.management_inWork_result_change, name='management_inWork_result_change'),
    path('work_examine/', views01.work_examine, name='work_examine'),
    path('management_outWork_pass/', views01.management_outWork_pass, name='management_outWork_pass'),
    path('management_outWork_reject/', views01.management_outWork_reject, name='management_outWork_reject'),
    path('outWork_reject_result/', views01.outWork_reject_result, name='outWork_reject_result'),
    path('outWork_reject_result_send/', views01.outWork_reject_result_send, name='outWork_reject_result_send'),


    path('interview_list/', views01.interview_list, name='interview_list'),
    path('notice_send/', views01.notice_send, name='notice_send'),
    path('back_reason/', views01.back_reason, name='back_reason'),
    path('interview_result/', views01.interview_result, name='interview_result'),
    path('stu_result/', views01.stu_result, name='stu_result'),
    path('company_list/', views01.company_list, name='company_list'),


    # path('<CharField:manager_id>/results/', views01.results, name='results'),
    # path('<CharField:manager_id/vote/', views01.vote, name='vote'),

]