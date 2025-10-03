from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class ForceDefaultLanguageMiddleware(MiddlewareMixin):
    """
    Ignoruje nagłówek Accept-Language, ale pozwala na ustawienie języka przez /set-language/.
    """

    def process_request(self, request):
        # Pozwól na POST do set_language
        if request.path == '/set-language/' and request.method == 'POST':
            return

        # Usuń nagłówek Accept-Language dla pozostałych stron
        request.META.pop('HTTP_ACCEPT_LANGUAGE', None)

        # Wymuś domyślny język jeśli nie ustawiono w sesji ani cookie
        if not request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME):
            request.LANGUAGE_CODE = settings.LANGUAGE_CODE