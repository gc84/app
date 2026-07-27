import os
import dj_database_url

# Troque a linha do SECRET_KEY por:
SECRET_KEY = os.environ.get('SECRET_KEY', 'chave-provisoria-so-para-teste-local')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']  # depois trocamos pelo domínio real

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # adicione essa linha logo abaixo da anterior
    # ... resto do middleware que já existe, sem mexer
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Banco de dados: usa Postgres se houver DATABASE_URL, senão usa sqlite local
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600,
    )
}