import random

from django.http import HttpResponseRedirect
from django.urls import reverse

from myapp.models import UserTicket


def get_ticket():
    s = '0123456789abcdefghijklmnopqrstuvwxyz'
    ticket = ''
    for i in range(25):
        ticket += random.choice(s)

    return ticket


def is_login(func):
    def check(request):
        ticket = request.COOKIES.get('ticket')
        if ticket:
            user_ticket = UserTicket.objects.filter(ticket=ticket).first()
            if user_ticket:
                return func(request)
            else:
                # ticket参数错误
                return HttpResponseRedirect(reverse('myapp:login'))
        else:
            return HttpResponseRedirect(reverse('myapp:login'))
    return check
