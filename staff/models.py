from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.utils.text import slugify


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
    subheader = models.CharField(verbose_name='Funkcja', max_length=150)
    description = HTMLField(blank=True, null=True,  verbose_name='Nagłówki pod nawziskiem (pole listy)')
   
    active = models.BooleanField(default=True, verbose_name='aktywny')

    objects = models.Manager()
    activated = ActiveManager()

    

    def gallery_main_image(self):
        main = self.gallery.filter(is_main=True).first()
        if main:
            return main.image.url  # lub main.image.name jeśli chcesz tylko nazwę
        return "-"
   

    def gallery_images(self):
        return ", ".join([g.image.url for g in self.gallery.all()])

    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staff'
        ordering = ('order',)



    def __str__(self):
        return self.name
    
class Profile(models.Model):
    person = models.OneToOneField(Person,on_delete=models.CASCADE,null=True, blank=True)
    o_mnie = HTMLField(verbose_name='O mnie')
    
    procedury_intro = HTMLField(blank=True, null=True,  verbose_name='procedury nagłówek')
    procedury = HTMLField(blank=True, null=True,  verbose_name='Procedury')
    
    rekomendacje_intro = HTMLField(blank=True, null=True,  verbose_name='rekomendacje nagłówek')
    kalendarium_intro = HTMLField(blank=True, null=True,  verbose_name='kalendarium nagłówek')
    
    def __str__(self):
        return f'Profil szczegółowy {self.person.name}'
    
class Gallery(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="gallery",null=True, blank=True)
    image = models.ImageField(upload_to="gallery/", null=True, blank=True)
    is_main = models.BooleanField(default=False)  # główne zdjęcie
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Galeria'

class Rekomendacja(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="rekomendacja",null=True, blank=True)
    image = models.ImageField(upload_to="rekomendacje/", null=True, blank=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    
    name = models.CharField(max_length=200)
    desc1 = models.CharField(max_length=100)
    desc2 = models.CharField(max_length=100)
    rekomendacja_content = HTMLField()

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Rekomendacje'

    def __str__(self):
        return f'Rekomendacja dla {self.profile.person.name} od {self.name}'


class Event(models.Model):
    MONTH_CHOICES = [
        (1, "Styczeń"),
        (2, "Luty"),
        (3, "Marzec"),
        (4, "Kwiecień"),
        (5, "Maj"),
        (6, "Czerwiec"),
        (7, "Lipiec"),
        (8, "Sierpień"),
        (9, "Wrzesień"),
        (10, "Październik"),
        (11, "Listopad"),
        (12, "Grudzień"),
    ]

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="kalendarium",
        null=True, blank=True
    )

    year = models.PositiveIntegerField(validators=[MinValueValidator(1950),MaxValueValidator(datetime.date.today().year + 5)],verbose_name="Rok")
    month = models.PositiveSmallIntegerField(
        choices=MONTH_CHOICES,
        null=True,
        blank=True,
        verbose_name="Miesiąc"
    )
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    content = HTMLField(verbose_name="Treść")

    class Meta:
        ordering = ["-year", "-month", "title"]
        verbose_name = "Kalendarium"
        verbose_name_plural = "Kalendarium"

    def __str__(self):
        if self.month:
            return f" ({self.month}/{self.year}) {self.title}"
        return f" ({self.year}) {self.title}"










