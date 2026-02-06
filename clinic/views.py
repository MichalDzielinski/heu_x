from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from services.models import Procedura
from django.db.models import Q
from django.core.mail import EmailMessage

from django.http import JsonResponse
from django.views.generic.edit import FormView
from .forms import ContactForm

from django.shortcuts import render, redirect
from django.utils.translation import activate, get_language
from django.urls import resolve, reverse
from django.http import HttpResponse

from django.contrib.postgres.search import SearchVector
from django.utils import translation

from staff.models import Person

class IndexView(TemplateView):
    template_name='clinic/indxxx4.html'
   
class BadanieUrodynamiczneView(DetailView):
    template_name='clinic/badanie_urodynamiczne.html'
    model = Procedura

    def get_object(self):
        return get_object_or_404(Procedura, pk=1)

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

class WyszukajView( ListView):
    model = Procedura
    
    template_name = 'clinic/wyszukaj.html'

    def get_queryset(self):
        current_language = translation.get_language()
        search_field_1 =f'nazwa_{current_language}'
        search_field_2 =f'opis_{current_language}'
        search_field_3 =f'wskazania_{current_language}'


        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.annotate(search=SearchVector(search_field_1, search_field_2, search_field_3, 'lekarz')).filter(active=True).filter(search=query)
        else:
            queryset = Procedura.activated.all()
        return queryset
       
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')  # Pass query back to template for form value
        return context

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
    template_name = 'clinic/jak_nas_znalezc.html'

class WizytaView(TemplateView):
    template_name = 'clinic/wizyta.html'

class ZespolView(ListView):
    template_name = 'clinic/zespol.html'

    context_object_name = 'query'  # optional: defaults to 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doktor'] = Person.activated.filter(typ='lekarz')
        context['rehabilitant'] = Person.activated.filter(typ='rehabilitant')
        context['manager'] = Person.activated.filter(typ='manager')
        
        return context




    def get_queryset(self):
        # Only return available productsj
        return Person.activated.all()

class PersonView(DetailView):
    model = Person
    template_name = 'clinic/person.html'
    slug_field = 'id'      # pole w modelu
    slug_url_kwarg = 'id'  # parametr z URL


class StrefaView(TemplateView):
    template_name = 'clinic/strefa.html'

class ContactView(FormView):
    form_class = ContactForm
    template_name = "elements/contact/contact-form.html"  # <- używasz gdzie chcesz
    success_url = "/"

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        topic = form.cleaned_data["topic"]
        temat = form.cleaned_data['temat']

        recipients = {
            "urologia": "urologia.czynnosciowa+urologia@gmail.com",
            "kardiologia": "urologia.czynnosciowa+kardiologia@gmail.com",
            "rehabilitacja": "urologia.czynnosciowa+rehabilitacja@gmail.com",
        }

        # recipient = recipients.get(topic, "urologia.czynnosciowa@gmail.com")
        recipient = recipients.get('urologia.czynnosciowa@gmail.com', "urologia.czynnosciowa@gmail.com")

       

        mail = EmailMessage(
            subject=f'{temat} [{topic}]',
            body=message,
            from_email='urologia.czynnosciowa@gmail.com',
            
            to=[recipient],
            reply_to=[email],
        
           
        )
        mail.send()
        return JsonResponse({"ok": True})

    def form_invalid(self, form):
        return JsonResponse({"ok": False, "errors": form.errors}, status=400)
