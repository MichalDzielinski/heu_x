from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField

class CustomUser(AbstractUser):
    pass

class ActiveManager(models.Manager):
    def get_queryset(self):
        return (super().get_queryset().filter(active=True))

class Person(models.Model):
    name = models.CharField(max_length=75, verbose_name='Nazwisko')
    # main_photo = models.ImageField(upload_to='photos/', default='img/blank-profile-picture.png', verbose_name='zdjęcie')
    active = models.BooleanField(default=True, verbose_name='aktywny')
    order = models.PositiveIntegerField(verbose_name='kolejność')

    # typ = models.CharField(max_length=75, null=True, blank=True)

    # line_1 = models.CharField(max_length=256, verbose_name='Nagłówek (linia pierwsze)')
    # line_2 = models.CharField(max_length=256, blank=True,null=True, verbose_name='Nagłówek (linia druga)')
    # line_3 = models.CharField(max_length=256, blank=True,null=True, verbose_name='Nagłówek (linia trzecia)')
    # line_4 = models.CharField(max_length=256, blank=True,null=True, verbose_name='Nagłówek (linia czwarta)') 
    # line_5 = models.CharField(max_length=256, blank=True,null=True, verbose_name='Nagłówek (linia piąta)')

    # desc_1 = HTMLField(blank=True, null=True,  verbose_name='Opis')
   

    objects = models.Manager()
    activated = ActiveManager()

    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staff'
        ordering = ('order',)



    def __str__(self):
        return self.name