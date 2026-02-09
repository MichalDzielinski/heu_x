from modeltranslation.translator import translator, TranslationOptions
from .models import Person

class PersonTranslationOptions(TranslationOptions):
    fields = (

        'subheader',
        'description',
       
    
        )

translator.register(Person, PersonTranslationOptions)