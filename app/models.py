from django.db import models



class Jamoa(models.Model):
    logotip = models.ImageField(upload_to='jamoa_rasm')
    jamoa_nomi = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='jamoa_rasm')
    malumot = models.TextField()
    shior = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100)
    sana = models.DateField()
    telefon = models.IntegerField()
    muallif = models.CharField(max_length=200)


    albom1 = models.ImageField(upload_to='jamoa_rasm', null=True, blank=True)
    albom2 = models.ImageField(upload_to='jamoa_rasm', null=True, blank=True)
    albom3 = models.ImageField(upload_to='jamoa_rasm', null=True, blank=True)
    albom4 = models.ImageField(upload_to='jamoa_rasm', null=True, blank=True)
    
    def __str__(self):
        return f"{self.jamoa_nomi} | {self.email} | {self.telefon}"

    class Meta:
        verbose_name = 'Jamoa'
        verbose_name_plural = "Jamoa"


class Xizmat(models.Model):
    rasm = models.ImageField(upload_to='blog_rasm')
    nomi = models.CharField(max_length=200)
    malumot = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.nomi}"

    class Meta:
        verbose_name = 'Xizmat'
        verbose_name_plural = "Xizmatlar"


class Ishtirokchi(models.Model):
    rasm = models.ImageField(upload_to='ishtirokchi_rasm', null=True, blank=True)
    ism_sharif = models.CharField(max_length=200)
    tugilgan_yil = models.DateField(null=True, blank=True)
    manzil = models.CharField(max_length=200, null=True, blank=True)
    telefon = models.IntegerField()
    telegram = models.CharField(max_length=1000)
    instagram = models.CharField(max_length=1000)


    def __str__(self):
        return f"{self.ism_sharif} | {self.tugilgan_yil} | {self.manzil} | {self.telefon}"

    class Meta:
        verbose_name = "Ishtirokchi"
        verbose_name_plural = "Ishtirokchilar"



class Statistika(models.Model):
    nomi = models.CharField(max_length=200)
    soni = models.IntegerField()

    def __str__(self):
        return f"{self.nomi} | {self.soni}"

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistika"



class Blog(models.Model):
    rasm = models.ImageField(upload_to='blog_rasm', null=True, blank=True)
    mavzu = models.CharField(max_length=200)
    malumot = models.TextField(null=True, blank=True)
    vaqt = models.DateTimeField()
    soni = models.FloatField()

    def __str__(self):
        return f"{self.mavzu} | {self.vaqt} | {self.soni}"

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"
    

class Portfolio(models.Model):
    rasm = models.ImageField(upload_to='portfolio_rasm')
    nom = models.CharField(max_length=200)
    izoh = models.TextField()


    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfoliolar"
    

class Mijoz_fikri(models.Model):
    rasm = models.ImageField(upload_to='blog_rasm', null=True, blank=True)
    ism_sharif = models.CharField(max_length=200)
    izoh = models.TextField()

    def __str__(self):
        return self.ism_sharif
    

    
    
class Video_darslar(models.Model):
    nomi = models.CharField(max_length=200)
    muallif = models.CharField(max_length=200)
    link = models.URLField(help_text="youtu.be ning o'rniga youtube.com/embed so'zini kiriting")
    sana = models.DateField(max_length=200)
    
    
    
    def __str__(self):
            return f"{self.nomi}  | {self.link} | {self.sana} " 
        
    class Meta:
        verbose_name = 'Video dars'
        verbose_name_plural = 'Video darslar'