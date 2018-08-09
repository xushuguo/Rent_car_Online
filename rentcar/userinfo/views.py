import logging

from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render, redirect
from pymysql import DatabaseError

from userinfo.models import UserInfo

auth_check = 'MarcelArhut'

# Create your views here.
def signin(request):
    return render(request, 'login.html')

def register_in(request):
    return render(request, 'register.html')

def register_(request):
    if request.method == 'POST':
        new_user = UserInfo()
        new_user.uname = request.POST.get('user_namae')
        try:
            a = UserInfo.objects.get(uname=new_user.uname)
            if a:
                return render(request, 'register.html', {'messageuanme':'该用户不存在'})

        except ObjectDoesNotExist as e:
            logging.warning(e)
        if request.POST.get('pwd') != request.POST.get('cpwd'):
            return render(request, 'register.html', {'message_':'两次输入的密码不一致'})
        new_user_pwd = make_password(request.POST.get('pwd'), auth_check, 'pbkdf2_sha1')
        new_user.upassword = new_user_pwd
        new_user.email = request.POST.get('email')

        try:
            new_user.save()
        except DatabaseError as e:
            logging.warning(e)
        return render(request, 'index.html')
    return redirect('/user/register')

def login_(request):
    if request.method == 'POST':
        user = UserInfo()
        user.uname = request.POST.get('pwd')
        try:
            find_user = UserInfo.objects.filter(uname=user.uname)
            if len(find_user) <= 0:
                messages.add_message(request, messages.ERROR, '该用户未注册')
                return redirect('/user/login/')
            if not check_password(user.upassword, find_user[0].upassword):
                return render(request, 'login.html', {'user_info':user,'message_error':'用户名或者密码错误'})
        except ObjectDoesNotExist as e:
            logging.warning(e)
        request.session['user_id'] = find_user[0].id
        request.session['user_name'] = user.uname
        if request.COOKIES.get('url'):
            url = request.COOKIES.get('url')
            res = redirect('url')
            return res
        return redirect('/')
    return redirect('/user/login/')

def login_out(request):
    try:
        if request.session['user_name']:
            del request.session['user_id']
            del request.session['user_name']
    except KeyError as e:
        logging.warning(e)
    return redirect('/')