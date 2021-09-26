from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('create/project', views.ProjectCreateAPIView.as_view() , name = 'createproject'),
    path('create/subproject', views.SubprojectCreateAPIView.as_view() , name = 'createsubproject'),
    path('view/project', views.ProjectListAPIView.as_view() , name = 'createproject'),
    path('view/subproject', views.SubprojectListAPIView.as_view() , name = 'createsubproject'),


]