from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import *
from .tokens import account_activation_token

from .models import ClientType


"""
BASIC FUNCTIONALITY-------------------------------------------------------------
"""
def portal(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request, 'tools/portal-staff.html')
        if request.user.profile.client_type.client_type == 'student':
            return render(request, 'tools/portal-student.html')
        return render(request, 'tools/portal-web.html', context={
                        'username' : request.user.username
                        })
    return render(request, 'tools/portal.html')


def pagelogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('tools:portal')


"""
USER REGISTRATION AND AUTHORIZATION---------------------------------------------
"""
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Active your Wright Minded account!'
            message = render_to_string('registration/account_activation_email.html', {
                'user' : user,
                'domain' : current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token' : account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form' : form})


def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.profile.payrate = 0
        user.profile.enrollment_status = 'web'
        user.profile.client_type = ClientType.objects.get(pk=1)
        user.save()
        login(request, user)
        return redirect('tools:portal')
    else:
        return render(request, 'registration/account_activation_invalid.html')


"""
USER PROFILE--------------------------------------------------------------------
"""
@login_required
def profile(request):
    user = request.user
    profile = request.user.profile
    return render(request, 'users/profile.html', {'user' : user, 'profile' : profile})


@login_required
def profile_edit(request):
    user = request.user
    profile = request.user.profile
    if request.method == 'POST':
        form_basic = UserProfileBasic(request.POST, instance=user)
        form_profile = UserProfile(request.POST, instance=profile)
        if form_basic.is_valid() and form_profile.is_valid():
            form_basic.save()
            form_profile.save()
            return redirect('tools:profile')
        return redirect('tools:profile_edit')
    else:
        form_basic = UserProfileBasic(initial={
                                        'first_name' : user.first_name,
                                        'last_name' : user.last_name,
                                        'email' : user.email})
        form_profile = UserProfile(initial={
                                    'phone_number' : profile.phone_number,
                                    'address1' : profile.address1,
                                    'address2' : profile.address2,
                                    'city' : profile.city,
                                    'state': profile.state,
                                    'zipcode' : profile.zipcode})
    return render(request, 'users/profile-edit.html', {'form_basic' : form_basic, 'form_profile' : form_profile, 'username' : user.username})

# @login_required
# def profile_edit(request):
#     user = request.user
#     profile = request.user.profile
#     if request.method == 'POST':
#         if request.user.is_staff:
#             form_basic = UserProfileBasic(request.POST, instance=user)
#             form_profile = UserProfileStaff(request.POST, instance=profile)
#             if form_basic.is_valid() and form_profile.is_valid():
#                 form_basic.save()
#                 form_profile.save()
#         if request.user.profile.client_type.client_type == 'student':
#             form_basic = UserProfileBasic(request.POST, instance=user)
#             form_profile = UserProfileStudent(request.POST, instance=profile)
#             if form_basic.is_valid() and form_profile.is_valid():
#                 form_basic.save()
#                 form_profile.save()
#         else:
#             form_basic = UserProfileBasic(request.POST, instance=user)
#             form_profile = UserProfileWeb(request.POST, instance=profile)
#             if form_basic.is_valid() and form_profile.is_valid():
#                 form_basic.save()
#                 form_profile.save()
#         redirect('tools:profile')
#     else:
#         if request.user.is_staff:
#             form_profile = UserProfileStaff()
#         if request.user.profile.client_type.client_type == 'student':
#             form_profile = UserProfileStudent()
#         else:
#             form_profile = UserProfileWeb()
#     return render(request, 'users/profile-edit.html', {
#                 'form_basic' : form_basic,
#                 'form_profile' : form_profile,
#                 'username' : user.username})
