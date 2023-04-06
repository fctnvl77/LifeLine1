from django.shortcuts import render

# Create your views here.


from django.views.generic import ListView
from .models import Mijoz_fikri, Blog,Ishtirokchi,Jamoa,Portfolio,Statistika,Xizmat,Video_darslar


class JamoaViews(ListView):
    model = Ishtirokchi
    template_name = "jamoa.html"
    context_object_name = "Komanda"


class VideoViews(ListView):
    model = Video_darslar
    template_name = "video.html"
    context_object_name = "Video"




# def video(request):
#    allItems= Video_darslar.objects.all()
#    context= {'allitems': allItems}
#    return render(request, 'video.html', context)

def index(request):
    jamoa = Jamoa.objects.all()
    ishtirokchi = Ishtirokchi.objects.all()
    statistika = Statistika.objects.all()
    xizmat = Xizmat.objects.all()
    mijoz = Mijoz_fikri.objects.all()
    portfolio = Portfolio.objects.all()
    contex = {
        'Jamoa':jamoa,
        'Ishtirokchi':ishtirokchi,
        'Statistika':statistika,
        'Xizmat':xizmat,
        'Mijoz':mijoz,
        'Portfolio':portfolio,
    }
    return render(request, ['index.html', 'xizmat.html', 'jamoa.html', 'mijoz.html', 'portfolio.html'], contex)