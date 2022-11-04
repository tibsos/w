from django.urls import path

from django.contrib.auth.views import LogoutView as LV

from django.conf import settings as s

from .views import *

app_name = 'u'

urlpatterns = [

    path('login/', l, name='li'),
    path('logout/', LV.as_view(), {'next_page': s.LOGOUT_REDIRECT_URL} ,name='lo'),
    path('register/', r, name='r'),
    path('forgot-password/', l, name='fp'),

]