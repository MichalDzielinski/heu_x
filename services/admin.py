from django.contrib import admin
from .models import Procedura
from django.utils.html import format_html
from django import forms
from django.utils.safestring import mark_safe

class SuffixTextInput(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'style': 'width: 60px;'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        return mark_safe(f'{html} <span style="margin-left:5px;">zł</span>')
    
class SuffixTextInput2(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'style': 'width: 55px;'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        return mark_safe(f'{html} <span style="margin-left:5px;">dni</span>')
    
class SuffixTextInput3(forms.TextInput):

    def __init__(self, attrs=None):
        default_attrs = {'style': 'width: 55px;'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        return mark_safe(f'{html} <span style="margin-left:5px;">minut</span>')
    
class ProceduraAdminForm(forms.ModelForm):
    class Meta:
        model = Procedura
        fields = '__all__'
        widgets = {
            'koszt': SuffixTextInput(),
            'czas_oczekiwania': SuffixTextInput2(),  
            'czas_badania': SuffixTextInput3(),  
        }

@admin.register(Procedura)
class ProceduraAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'active', 'czas_oczekiwania', 'czas_badania_min', 'koszt', 'nazwa_summary', 'opisy_summary', 'instruktaż_summary')
    list_editable = ('czas_oczekiwania','koszt','active',)
    list_filter = ['lekarz', 'specjalizacja']
    search_fields = ['opis', 'wskazania']
    ordering = ['order',]
    form = ProceduraAdminForm

    fieldsets = (
        (None, {
            'fields': ['nazwa', 'specjalizacja', 'typ_usługi', 'lekarz', 'active', 'order','czas_oczekiwania','czas_badania', 'cena_od',  'koszt'],
            'classes': ['wide'],
        }),

          
          ('OPIS', {
            'fields': ['opis_pl','polega_pl','przebieg_pl', 'wskazania_pl', 'after_pl'],
            'classes': ['collapse'],
        }),
        ('OPIS po angielsku', {
            'fields': ['nazwa_en', 'opis_en','polega_en','przebieg_en', 'wskazania_en', 'after_en'                       ],
            'classes': ['collapse'],

        }),
        ('OPIS po ukraińsku', {
            'fields': ['nazwa_uk', 'opis_uk','polega_uk','przebieg_uk', 'wskazania_uk', 'after_uk'],
            'classes': ['collapse'],
        
        }),
          
   

           ('DOKUMENTY', {
              'fields': ['pdf_pl','pdf_en','pdf_uk'],
              'classes': ['collapse'],
          }),
        

       )
    
    @admin.display(description='Opisy [PL/EN/UKR]')
    def opisy_summary(self, obj):
            def colored_icon(value):
                icon = '✅' if value else '❌'
                
                color = 'green' if value else 'red'
                return format_html('<span style="color: {}; font-weight: bold; font-family: sans-serif;">{}</span>', color, icon)

            return format_html(
                    '{} {} {}',
                    colored_icon(obj.opis_pl),
                    colored_icon(obj.opis_en),
                    colored_icon(obj.opis_uk),
            )

    @admin.display(description='Instruktaż [PL/EN/UKR]')
    def instruktaż_summary(self, obj):
            def colored_icon(value):
                icon = '✅' if value else '❌'
                
                color = 'green' if value else 'red'
                return format_html('<span style="color: {}; font-weight: bold; font-family: sans-serif;">{}</span>', color, icon)

            return format_html(
                    '{} {} {}',
                    colored_icon(obj.pdf_pl),
                    colored_icon(obj.pdf_en),
                    colored_icon(obj.pdf_uk),
            )
        
    @admin.display(description='Nazwa [PL/EN/UKR]')
    def nazwa_summary(self, obj):
            def colored_icon(value):
                icon = '✅' if value else '❌'
                
                color = 'green' if value else 'red'
                return format_html('<span style="color: {}; font-weight: bold; font-family: sans-serif;">{}</span>', color, icon)

            return format_html(
                    '{} {} {}',
                    colored_icon(obj.nazwa_pl),
                    colored_icon(obj.nazwa_en),
                    colored_icon(obj.nazwa_uk),
            )

    def czas_badania_min(self, obj):
        return f"{obj.czas_badania} minut"
  


   