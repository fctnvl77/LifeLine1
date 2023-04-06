
from django.urls import path

from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', index, name='index'),
    path('jamoa', JamoaViews.as_view(), name='jamoa'),
    path('video', VideoViews.as_view(), name='video'),
    # path('video', video, name='video')
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
