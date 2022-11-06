from django.urls import path

from .views import *

app_name = 'a'

urlpatterns = [

    path('home/', h, name='h')

]

htmx_urlpatterns = [

    path('cn', cn, name='cn'),
    path('p', p, name='p'),
    path('d', d, name='d'),

]

ajax_urlpatterns = [

    path('t', t, name='t'),
    path('c', c, name='c'),
    path('a', a, name='a'),

]

urlpatterns += htmx_urlpatterns
urlpatterns += ajax_urlpatterns