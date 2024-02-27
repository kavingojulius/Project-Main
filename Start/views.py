from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):

    # if request.method == 'GET':
    work = ImagesWork.objects.all()
    video_work = VideosWork.objects.all()
    
    context = {
        'work' : work,
        'video_work' : video_work
    }

    

    return render(request, 'mainpages/home.html', context )