from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from myapp.forms import UserForm
from myapp.models import Users, UserTicket
from utils.functions import get_ticket, is_login


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            password = make_password(form.cleaned_data['password'])
            Users.objects.create(username=form.cleaned_data['username'], password=password)

            return HttpResponseRedirect(reverse('myapp:login'))

        else:
            return render(request, 'register.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            # 登录的设置
            # 1.通过用户名和密码获取当前的user对象  ====>> auth.authenticate()
            user = Users.objects.filter(username=form.cleaned_data['username']).first()
            if user:
                # 将user.password和form.cleaned_data['password']进行校验
                if check_password(form.cleaned_data['password'], user.password):
                    # 校验成功
                    # 1.向cookie中设置随机参数ticket
                    res = HttpResponseRedirect(reverse('myapp:index'))
                    # set_cookie(key, value, max_age='', expires='')
                    ticket = get_ticket()
                    res.set_cookie('ticket', ticket, max_age=10)
                    # 2.向user_ticket中存这个ticket和user的对应关系
                    UserTicket.objects.create(user=user, ticket=ticket)

                    return res

                else:
                    return render(request, 'login.html')
            else:
                # 用户名不存在
                return render(request, 'login.html')
            # 2.设置cookie中的随机值  =====>> auth.login()
            # 3.设置user_ticket中的随机值
        else:
            return render(request, 'login.html')


# @is_login
def index(request):
    if request.method == 'GET':
        # ticket = request.COOKIES.get('ticket')
        # user_ticket = UserTicket.objects.filter(ticket=ticket).first()
        # if user_ticket:
        #     user = user_ticket.user
        #     return render(request, 'index.html', {'user':user})
        # else:
        #     return HttpResponseRedirect(reverse('myapp:login'))
        return render(request, 'index.html')