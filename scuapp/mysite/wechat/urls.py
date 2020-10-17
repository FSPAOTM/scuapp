from django.urls import path

from . import views

app_name = 'wechat'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<manager_id>/', views.detail, name='detail'),
    path('dengluzhuce_login/', views.dengluzhuce_login, name='dengluzhuce_login'),
    path('Manage_register/', views.Manage_register, name='Manage_register'),
    path('Student_register/', views.Student_register, name='Student_register'),
    path('Company_register/', views.Company_register, name='Company_register'),
    #path('<CharField:manager_id>/results/', views.results, name='results'),
    #path('<CharField:manager_id/vote/', views.vote, name='vote'),
]