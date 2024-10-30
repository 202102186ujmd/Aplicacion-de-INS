from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ex$wxy(pw$7h$@&ujciwxi1f6^sn%vp8x40!y)&oqmtooizmq5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Asegúrate de agregar los hosts que vas a usar en producción
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Tu aplicación personalizada
    'eventos',  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EventosINS.urls'

# Asegúrate de que las plantillas apunten correctamente a la carpeta de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'eventos', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'EventosINS.wsgi.application'

# Base de datos MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestion_eventos2',  
        'USER': 'eventos2',          
        'PASSWORD': 'eventos2',      
        'HOST': 'localhost',         
        'PORT': '3306',              
    }
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'eventos', 'static'),
]

# Configuración para usar claves automáticas grandes
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirección después del login
LOGIN_REDIRECT_URL = '/admin_dashboard/'  # Cambié a 'home' para redirigir a la página principal
LOGOUT_REDIRECT_URL = '/'  # Redirigir a home después del logout
LOGIN_URL = '/login/'  # URL para el formulario de login

# Configuración de correo para recuperación de contraseña
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'proyectoeventosins@gmail.com'
EMAIL_HOST_PASSWORD = 'ticp kpfz ywzg lofz'
DEFAULT_FROM_EMAIL = 'proyectoeventosins@gmail.com'

# Modelo de usuario personalizado
AUTH_USER_MODEL = 'eventos.User'  # Modelo de usuario personalizado

