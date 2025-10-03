from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name',  'typ', 'active']
    list_editable = ['active']

    # readonly_fields = ['photo_tag_2']
    # summernote_fields = ('desc_1_pl', 'desc_1_en', 'desc_1_uk',)
