from modeltranslation.translator import translator, TranslationOptions
from .models import Procedura

class ProceduraTranslationOptions(TranslationOptions):
    fields = (

        'nazwa',
        'opis',
        'polega',
        'przebieg',
        'wskazania',
        'after'
    
        )

translator.register(Procedura, ProceduraTranslationOptions)

