print("using local settings")

DEBUG = True

SECURE_SSL_REDIRECT = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ema_dec_26_2017',
        'USER': 'postgres',
        'PASSWORD': 'omar2222',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}