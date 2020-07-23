from django.contrib import admin
from django.urls import path, include
from members import views

urlpatterns = [
    path('memberlist/', views.memberlist, name='memberlist'),
    path('<int:member_id>/', views.detail, name='memberdetail'),
    path('addmember', views.addmember, name='addmember')
]