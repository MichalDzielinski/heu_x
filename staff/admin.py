from django.contrib import admin
from .models import Person, Profile, Gallery, Rekomendacja, Event
from django.utils.html import format_html

class GalleryInline(admin.TabularInline):
    model = Gallery
   
class KalendariumInline(admin.StackedInline):
    model = Event
    
class RekomendacjaInline(admin.StackedInline):
    model = Rekomendacja

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo_tag',  'typ', 'active']
    list_editable = ['active']
    readonly_fields = ['photo_tag_2']
    
    def photo_tag(self, obj):
        if obj.main_photo:
            return format_html('<img src="{}"  style="width: 45px; height: 45px; border-radius: 50%; object-fit: cover;" />', obj.main_photo.url)
        return "-"
    photo_tag.short_description = 'Bieżące zdjęcie'

    def photo_tag_2(self, obj):
        if obj.main_photo:
            return format_html('<img src="{}"  style="width: 125px; height: 125px; border-radius: 50%; object-fit: cover;" />', obj.Main_photo.url)
        return "-"
    photo_tag_2.short_description = 'Bieżące zdjęcie'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, RekomendacjaInline, KalendariumInline ]
