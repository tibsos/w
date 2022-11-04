from django.urls import path

from .views import *

app_name = 'a'

urlpatterns = [

    path('home/', h, name='h')

]

htmx_urlpatterns = [

    path('cn', cn, name='cn'), # create note

    path('p', p, name='p'), # pin note

    path('d/<uuid:uid>/', d, name='d'), # delete note

]

ajax_urlpatterns = [

    path('t', t, name='t'), # update title
    path('c', c, name='c'), # update content

]

urlpatterns += htmx_urlpatterns
urlpatterns += ajax_urlpatterns