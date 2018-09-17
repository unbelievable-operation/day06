from django.conf.urls import url

from myapp import views

urlpatterns = [
    url(r'register/', views.register, name='register'),
    url(r'login/', views.login, name='login'),
    url(r'index/', views.index, name='index'),
]