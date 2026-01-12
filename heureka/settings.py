from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
import os


load_dotenv()

#region DEPLOYMENT SETTINGS
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = []
# WSGI_APPLICATION = "heureka.wsgi.application"
#endregion

#region BASE SETTINGS

ROOT_URLCONF = "heureka.urls"
AUTH_USER_MODEL = 'staff.CustomUser'
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#endregion 

INSTALLED_APPS = [
    "modeltranslation",
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    #third party apps
    'storages',
    "tinymce",
    "tailwind",
    "theme",
    "widget_tweaks",
    'rosetta',
    
    #custom apps
    'clinic',
    'services',
    'staff',
]

#region TAILWIND SETTINGS
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
TAILWIND_APP_NAME = 'theme'

#endregion

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR, 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'clinic.context_processors.contact_form_context',
            ],
        },
    },
]

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )

}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

#region LANGUAGES & TIME
LANGUAGE_CODE = "pl"

LANGUAGES = [
    ('pl', 'Polski'),
    ('en', 'English'),
    ('uk', 'Ukrainian'),
]
MODELTRANSLATION_DEFAULT_LANGUAGE = 'pl'

LOCALE_PATHS = [
    BASE_DIR / 'locale'
]

TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_TZ = True
#endregion

#region STATIC & MEDIA FILES

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / 'theme/static']
# STATIC_URL = "https://4-doctor-ps.s3.eu-north-1.amazonaws.com/static/"
# STATICFILES_STORAGE = "heureka.storage_backends.StaticStorage"

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_ROOT = BASE_DIR / 'gallery'
MEDIA_URL = '/gallery/'
# DEFAULT_FILE_STORAGE = "heureka.storage_backends.MediaStorage"

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

#endregion

#region TINYMCE SETTINGS
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 610,
    'menubar': 'file edit view insert format tools table help',
    'plugins': 'advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table code help wordcount',
    'toolbar': 'undo redo | formatselect | bold italic underline | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
}

#endregion

#region JAZZMIN SETTINGS
JAZZMIN_SETTINGS = {
    "site_title": "Heureka Admin",
    "site_header": "Heureka Admin",
    "site_brand": "Heureka Admin",

}

#endregion



EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=True
# DEFAULT_FROM_EMAIL = 'Contact form <urologia.czynnosciowa@gmail.com>'



#region AWS S3 settings

STORAGES = {
    "default": {
        "BACKEND": "heureka.storage_backends.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "heureka.storage_backends.StaticStorage",
    },
}

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.environ.get(('AWS_S3_REGION_NAME'))

AWS_QUERYSTRING_AUTH = False






