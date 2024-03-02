from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('about_us', About_us, name='about_us')
]