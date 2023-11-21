from django.urls import path
from specific.views import *

app_name='nav'

urlpatterns= [
    path('sharuk/',sharuk,name='sharuk'),
    path('rithik/',rithik,name='rithik'),
]