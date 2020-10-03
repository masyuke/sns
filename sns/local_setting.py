import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'n_%ac^n_)+12^l43+#yqg1^87t!8&_g3r%mt@tp^d$7ngo3l2u'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sns_database',
        'USER': 'root',
        'PASSWORD': 'kenta',
        'HOST': 'localhost',
    }
}

DEBUG = True