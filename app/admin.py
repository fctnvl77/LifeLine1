from django.contrib import admin

# Register your models here.



from .models import Blog, Ishtirokchi, Jamoa, Mijoz_fikri, Portfolio, Statistika, Video_darslar, Xizmat 

admin.site.register(Jamoa)

admin.site.register(Ishtirokchi)

admin.site.register(Statistika)

admin.site.register(Xizmat)

admin.site.register(Blog)

admin.site.register(Portfolio)

admin.site.register(Mijoz_fikri)

# admin.site.register(Video_darslar)


admin.site.register(Video_darslar)