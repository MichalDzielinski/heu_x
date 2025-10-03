from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from clinic import views

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns( 

    path('lang/rosetta/', include('rosetta.urls')),
    path('tinymce/', include('tinymce.urls')),

    path("i18n/", include("django.conf.urls.i18n")),
    path('', include('clinic.urls')),  


    prefix_default_language=False

)

