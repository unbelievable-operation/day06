from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from myapp.models import UserTicket


class UserMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        # 排除不需要登录验证的地址
        # not_login_path = ['/myapp/login/', '/myapp/register/']
        # path = request.path
        # for n_path in not_login_path:
        #     if path == n_path:
        #         return None
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect(reverse('myapp:login'))

        user_ticket = UserTicket.objects.filter(ticket=ticket).first()
        if not user_ticket:
            return HttpResponseRedirect(reverse('myapp:login'))
        request.user = user_ticket.user
        return None
