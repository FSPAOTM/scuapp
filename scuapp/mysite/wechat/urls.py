from django.urls import path

from . import views

app_name = 'wechat'
urlpatterns = [
    #小程序界面
    path('', views.index, name='index'),
    path('detail/<manager_id>/', views.detail, name='detail'),
    path('dengluzhuce_login/', views.dengluzhuce_login, name='dengluzhuce_login'),
    path('Manage_register/', views.Manage_register, name='Manage_register'),
    path('Student_register/', views.Student_register, name='Student_register'),
    path('Company_register/', views.Company_register, name='Company_register'),
    path('Insert_resume/', views.Insert_resume, name='Insert_resume'),
    path('Reset_password/', views.Reset_password, name='Reset_password'),
    path('Reset_myinfo_name/', views.Reset_myinfo_name, name='Reset_myinfo_name'),
    path('Reset_myinfo_nickname/', views.Reset_myinfo_nickname, name='Reset_myinfo_nickname'),
    path('Reset_myinfo_phonenumber/', views.Reset_myinfo_phonenumber, name='Reset_myinfo_phonenumber'),
    path('Reset_myinfo_e_mail/', views.Reset_myinfo_e_mail, name='Reset_myinfo_e_mail'),

    #后台管理界面（网页）
    path('management_inWork_release/', views.management_inWork_release, name='management_inWork_release'),
    #path('<CharField:manager_id>/results/', views.results, name='results'),
    #path('<CharField:manager_id/vote/', views.vote, name='vote'),
]