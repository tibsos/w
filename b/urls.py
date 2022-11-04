from django.urls import path
from .views import l

app_name = 'b'

urlpatterns = [

    path('', l)

]