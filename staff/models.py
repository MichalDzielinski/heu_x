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
    main_photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='zdjęcie')
    order = models.PositiveIntegerField(verbose_name='kolejność')
    typ = models.CharField(max_length=75, null=True, blank=True)
    description = HTMLField(blank=True, null=True,  verbose_name='Nagłówki pod nawziskiem (pole listy)')
   
    active = models.BooleanField(default=True, verbose_name='aktywny')

    objects = models.Manager()
    activated = ActiveManager()

    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staff'
        ordering = ('order',)



    def __str__(self):
        return self.name