from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse 
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def Home(request):

    work = ImagesWork.objects.all()
    video_work = VideosWork.objects.all()
    service = Service.objects.all()  
    hero_images = HeroSection.objects.all()  

    page = Paginator(service, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    work_page = Paginator(work, 3)
    work_page_list = request.GET.get('page')
    work_page = work_page.get_page(work_page_list)

    video_page = Paginator(video_work, 3)
    video_page_list = request.GET.get('page')
    video_page = video_page.get_page(video_page_list)


    context = {
        # 'work' : work,
        # 'video_work' : video_work,
        'hero_images': hero_images,
        # 'service':service,
        'page': page,
        'work_page': work_page,
        'video_page': video_page,

        
    }

    return render(request, 'mainpages/home.html', context )


def About_us(request):

    return render(request, 'mainpages/about_us.html')

def Services(request):

    service = Service.objects.all()  

    context = {        
        'service':service,        
    }

    return render(request, 'mainpages/services.html', context)

def Portfolio(request):

    work = ImagesWork.objects.all()
    video_work = VideosWork.objects.all()

    context = {        
        'work' : work,
        'video_work' : video_work,
    }

    return render(request, 'mainpages/portfolio.html', context)

# def adminsignout(request):
#      logout(request)
#      return redirect(request, 'mainpages/home.html')