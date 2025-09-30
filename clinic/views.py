from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from services.models import Procedura
from django.db.models import Q


class IndexView(TemplateView):
    template_name='clinic/index.html'

class ProceduryView(TemplateView):
    template_name='clinic/procedury.html'

    pass
   
class BadanieUrodynamiczneView(DetailView):
    template_name='clinic/badanie_urodynamiczne.html'
    model = Procedura

    def get_object(self):
        return get_object_or_404(Procedura, pk=30)

class ProceduryUrlogiczneView(ListView):
    template_name='clinic/procedury_urologiczne.html'
    model = Procedura

    def get_queryset(self):
        return Procedura.activated.filter(specjalizacja='urologia')

class PozostałeProceduryView(ListView):
    template_name = 'clinic/pozostale_procedury.html'
    model = Procedura

    def get_queryset(self):
        return Procedura.activated.exclude(specjalizacja='urologia')

class ProceduryKardiologiczneView(ListView):
    template_name = 'clinic/procedury_kardiologiczne.html'
    model = Procedura

    def get_queryset(self):
        return Procedura.activated.filter(specjalizacja='kardiologia')

class ProceduryMedyczneView(ListView):
    template_name = 'clinic/procedury_medyczne.html'
    model = Procedura

    def get_queryset(self):
        return Procedura.activated.exclude(Q(specjalizacja='kardiologia')|Q(specjalizacja='urologia'))

class DoPobraniaView(TemplateView):
    template_name = 'clinic/do_pobrania.html'

class ProfilaktykaView(TemplateView):
    template_name = 'clinic/profilaktyka.html'

class PakietyView(TemplateView):
    template_name = 'clinic/pakiety.html'

class BadaniaKliniczneView(TemplateView):
    template_name = 'clinic/badania_kliniczne.html'

class KontaktView(TemplateView):
    template_name = 'clinic/kontakt.html'

class JakNasZnalezcView(TemplateView):
    template_name = 'clinic/jak_nas_znaleźć.html'

class WizytaView(TemplateView):
    template_name = 'clinic/wizyta.html'


class ZespolView(TemplateView):
    template_name = 'clinic/zespol.html'

    pass












