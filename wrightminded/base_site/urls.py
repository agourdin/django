from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('who-i-am/', views.who_i_am, name='who_i_am'),
    path('rates-and-services/', views.rates_and_services, name='rates_and_services'),
    path('the-hour-for-hour-promise/', views.the_hour_for_hour_promise, name='the-hour-for-hour-promise'),
    path('sign-up/', views.sign_up, name='sign-up'),
]
