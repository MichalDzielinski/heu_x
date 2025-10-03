from django.urls import path
from . import views



urlpatterns = [
    path("procedury", views.ProceduryView.as_view(), name='procedury'),
    path("badanie-urodynamiczne", views.BadanieUrodynamiczneView.as_view(), name='badanie urodynamiczne'),
    path("procedury-urologiczne", views.ProceduryUrlogiczneView.as_view(), name='procedury urologiczne'),
    path("pozostałe-procedury", views.PozostałeProceduryView.as_view(), name='pozostałe procedury'),
    path("procedury-kardiologiczne", views.ProceduryKardiologiczneView.as_view(), name='procedury kardiologiczne'),
    path("procedury-medyczne", views.ProceduryMedyczneView.as_view(), name='procedury medyczne'),
    
    path("do-pobrania", views.DoPobraniaView.as_view(), name='do pobrania'),
    path("profilaktyka", views.ProfilaktykaView.as_view(), name='profilaktyka'),
    path("pakiety", views.PakietyView.as_view(), name='pakiety'),
    path("badania-kliniczne", views.BadaniaKliniczneView.as_view(), name='badania kliniczne'),

    path("kontakt", views.KontaktView.as_view(), name='kontakt'),
    path("jak-nas-znalezc", views.JakNasZnalezcView.as_view(), name='jak nas znaleźć'),
    path("wizyta", views.WizytaView.as_view(), name='wizyta'),
    
    path("zespół", views.ZespolView.as_view(), name='zespół'),

    path("contact", views.ContactView.as_view(), name='contact'),

    path("", views.IndexView.as_view(), name='index'),


]

