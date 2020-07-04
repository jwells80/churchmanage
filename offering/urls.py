from django.urls import path
from offering import views


urlpatterns = [
    path('offeringlist/', views.offeringlist, name='offeringlist'),
    path('home/', views.home, name='home'),
    path('fund/', views.funds, name='fund'),
    path('mode/', views.payment, name='payment'),
    path('addpaytype/', views.addpaytype, name='addpaytype'),
    path('addfund/', views.addfund, name='addfund'),
    ]