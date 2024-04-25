from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse 
from .models import *

# Create your views here.

def Home(request):

    work = ImagesWork.objects.all()
    video_work = VideosWork.objects.all()
    service = Service.objects.all()  
    hero_images = HeroSection.objects.all()  

    context = {
        'work' : work,
        'video_work' : video_work,
        'service':service,
        'hero_images': hero_images
    }

    return render(request, 'mainpages/home.html', context )


def About_us(request):

    return render(request, 'mainpages/about_us.html' )


# def adminsignout(request):
#      logout(request)
#      return redirect(request, 'mainpages/home.html')