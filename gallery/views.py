from django.shortcuts import render,redirect
import datetime as dt
from django.http import HttpResponse,Http404
from .models import Image


# Create your views here.


def gallery(request):
    photos = Image.objects.all()
    return render(request,'all-photos/today-photos.html',{"photos":photos})
    


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
    

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/today-photos.html", {"image":image})