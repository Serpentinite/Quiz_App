import os
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'fu(#=zbh@9(dv8y%z3kuqar$n_@p-9@jka@=5loia(*3l28=nd'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}

DEBUG = True
