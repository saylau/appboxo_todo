import os
from .base import Base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Base):
    DEBUG = True

    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '1111')
    # Testing
    INSTALLED_APPS = Base.INSTALLED_APPS
    INSTALLED_APPS += ('django_nose',)
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package=apps'
    ]

    # Mail
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
