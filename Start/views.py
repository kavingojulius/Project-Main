from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

# Create your views here.

def Home(request):

    # if request.method == 'GET':
    work = ImagesWork.objects.all()
    video_work = VideosWork.objects.all()
    # paginator = Paginator(video_work, 2)
    # page_number = request.GET.get("page")
    # pagee = paginator.get_page(page_number)

    context = {
        'work' : work,
        'video_work' : video_work,
        
    }

    

    return render(request, 'mainpages/home.html', context )


def About_us(request):

    return render(request, 'mainpages/about_us.html' )