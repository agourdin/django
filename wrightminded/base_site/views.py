from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base_site/index.html')

def who_i_am(request):
    return render(request, 'base_site/who_i_am.html')

def rates_and_services(request):
    return render(request, 'base_site/rates_and_services.html')

def the_hour_for_hour_promise(request):
    return render(request, 'base_site/the_hour_for_hour_promise.html')

def sign_up(request):
    return render(request, 'base_site/sign_up.html')
