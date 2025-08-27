from pathlib import Path

#region DEPLOYMENT SETTINGS
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-32xta0ci*g*3w#x87@cr(2uzy^)1e4ef0t-=6^_e25@7_a=b$o"
DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = "heureka.wsgi.application"
#endregion

#region BASE SETTINGS

ROOT_URLCONF = "heureka.urls"
AUTH_USER_MODEL = 'staff.CustomUser'
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#endregion 

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    #third party apps
    "tailwind",
    'theme',
    
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
    "django.contrib.sessions.middleware.SessionMiddleware",
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
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
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
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_TZ = True
#endregion

#region STATIC & MEDIA FILES

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / 'theme/static']

#endregion


