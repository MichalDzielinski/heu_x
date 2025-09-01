from django.db import models
from tinymce.models import HTMLField


# active manager
class ActiveManager(models.Manager):
        def get_queryset(self):
            return (super().get_queryset().filter(active=True))

class Procedura(models.Model):
    
    class specjalizacja_choices(models.TextChoices):
        urologia = 'urologia', 'urologia'
        kardiologia = 'kardiologia', 'kardiologia'
        pulmunologia = 'pulmunologia', 'pulmunologia'
        rehabilitacja = 'rehabilitacja', 'rehabilitacja'
        inne = 'inne', 'inne'

    class typ_choices(models.TextChoices):
        badanie = 'B', 'badanie'
        zabieg = 'Z', 'zabieg'
        procedura = 'P', 'procedura'
        sesja = 's', 'sesja'

    class order_choices(models.TextChoices):
         A = 'A', 'A'
         B = 'B', 'B'
         C = 'C', 'C'
         D = 'D', 'D'
         E = 'E', 'E'
         F = 'F', 'F'

    nazwa = models.CharField(max_length=256)
    opis = HTMLField( blank=True, null=True, verbose_name='Opis badania')
    polega = HTMLField( blank=True, default='',  verbose_name='Na czym polega badanie')
    przebieg = HTMLField( blank=True, default='',  verbose_name='Przebieg badania')
    wskazania = HTMLField(blank=True, default='', verbose_name='Wskazania do badania [POLE LISTY]')
    after = HTMLField(blank=True, null=True, verbose_name='Po badaniu [POLE LISTY]')

    specjalizacja =  models.CharField(max_length=20, choices=specjalizacja_choices, default=specjalizacja_choices.urologia)
    typ_usługi = models.CharField(max_length=25, choices=typ_choices, default =typ_choices.badanie)
    order = models.CharField(max_length=1, choices=order_choices, default=order_choices.F, verbose_name='kolejność')
    active = models.BooleanField(default=False, verbose_name='aktywna')

    lekarz = models.CharField(max_length=200, blank=True, null=True)
    koszt = models.PositiveSmallIntegerField(blank=True, null=True)
    cena_od=models.BooleanField(default=False)
    czas_oczekiwania = models.IntegerField(blank=True, null=True)
    czas_badania = models.CharField(max_length=3, blank=True, null=True)

    pdf_pl = models.FileField(upload_to='downloads/', blank=True, null=True, verbose_name='Instruktaż po polsku' )
    pdf_en = models.FileField(upload_to='downloads/', blank=True, null=True, verbose_name='Instruktaż po angielsku')
    pdf_uk = models.FileField(upload_to='downloads/', blank=True, null=True, verbose_name='Instruktaż po ukraińsku')

    objects = models.Manager()
    activated = ActiveManager()

    class Meta:
        verbose_name_plural = 'procedury'
        ordering = ['order', 'nazwa']

    def __str__(self):
        return self.nazwa
    
    @property
    def dokumenty(self):
        return bool(self.pdf_pl or self.pdf_en or self.pdf_uk)
          
    @property
    def opisy(self):
        return bool(self.opis or self.polega or self.przebieg or self.wskazania)
        
    
