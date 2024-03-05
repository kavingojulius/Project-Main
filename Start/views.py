from django.shortcuts import render
from .models import *

# Create your views here.

def Home(request):

    work = ImagesWork.objects.all()
    video_work = VideosWork.objects.all()
    service = Service.objects.all()    

    context = {
        'work' : work,
        'video_work' : video_work,
        'service':service        
    }

    return render(request, 'mainpages/home.html', context )


def About_us(request):

    return render(request, 'mainpages/about_us.html' )