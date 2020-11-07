from django.urls import path

from . import views,views01

app_name = 'wechat'
urlpatterns = [
    #小程序界面
    path('detail/<manager_id>/', views.detail, name='detail'),
    path('dengluzhuce_login/', views.dengluzhuce_login, name='dengluzhuce_login'),
    path('Manage_register/', views.Manage_register, name='Manage_register'),
    path('Student_register/', views.Student_register, name='Student_register'),
    path('Company_register/', views.Company_register, name='Company_register'),
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
    path('Company_info_showmodiify/', views.Company_info_showmodiify, name='Company_info_showmodiify'),
    path('Company_info_modiify/', views.Company_info_modiify, name='Company_info_modiify'),
    path('Part_time_post/', views.Part_time_post, name='Part_time_post'),
    path('Get_outwork_info/', views.Get_outwork_info, name='Get_outwork_info'),
    path('Get_outwork_detail_info/', views.Get_outwork_detail_info, name='Get_outwork_detail_info'),
    path('Modify_outwork_info/', views.Modify_outwork_info, name='Modify_outwork_info'),
    path('Sget_outwork_info/', views.Sget_outwork_info, name='Sget_outwork_info'),
    path('Sget_outwork_detail_info/', views.Sget_outwork_detail_info, name='Sget_outwork_detail_info'),

    #后台管理界面
    path('', views01.index, name='index'),
    path('index/', views01.index, name='index'),
    path('login/', views01.login, name='login'),
    path('register/', views01.register, name='register'),
    path('inwork_list/', views01.inwork_list, name='inwork_list'),
    path('inwork_add/', views01.inwork_add, name='inwork_add'),
    path('inwork_foregetpwd/', views01.inwork_foregetpwd, name='inwork_foregetpwd'),
    path('management_login/', views01.management_login, name='management_login'),
    path('management_inwork_register/', views01.management_inwork_register, name='management_inwork_register'),
    path('management_forgetpwd/', views01.management_forgetpwd, name='management_forgetpwd'),
    # path('management_inWork_release_html/', views.management_inWork_release_html, name='management_inWork_release_html'),
    path('management_inWork_release/', views01.management_inWork_release, name='management_inWork_release'),
    # path('management_inWork_show/', views.management_inWork_show, name='management_inWork_show'),
    path('management_inWork_reset_show/', views01.management_inWork_reset_show, name='management_inWork_reset_show'),
    path('management_inWork_reset/', views01.management_inWork_reset, name='management_inWork_reset'),
    path('management_inWork_delete/', views01.management_inWork_delete, name='management_inWork_delete'),
    path('management_inWork_search/', views01.management_inwork_search, name='management_inWork_search'),


    # path('<CharField:manager_id>/results/', views.results, name='results'),
    # path('<CharField:manager_id/vote/', views.vote, name='vote'),

]