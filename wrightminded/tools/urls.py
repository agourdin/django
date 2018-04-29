from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import core_views

app_name = 'tools'
urlpatterns = [
    path('', core_views.portal, name='portal'),
    path('login/', auth_views.login, name='login'),
    path('logout/', core_views.pagelogout, name='logout'),
    path('sign-up/', core_views.signup, name='signup'),
    path('profile/', core_views.profile, name='profile'),
    path('profile/edit/', core_views.profile_edit, name='profile_edit')
]
