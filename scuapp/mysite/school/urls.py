from django.urls import path

from . import views

app_name = 'school'
urlpatterns = [
    path('', views.index, name='index'),
    path('<manager_id>/', views.detail, name='detail'),
    #path('<CharField:manager_id>/results/', views.results, name='results'),
    #path('<CharField:manager_id/vote/', views.vote, name='vote'),
]