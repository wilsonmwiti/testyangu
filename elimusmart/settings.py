# Generated by 'django-admin startproject' using Django 3.2.3.
from decouple import config
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS')

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'ckeditor',
    'mathfilters',
    'hijack_admin',
    'hijack',
    'compat',
    'simplemathcaptcha',
    'crispy_forms',
    'django_daraja',
    'tabular_permissions',
    'sorl.thumbnail',
    'tinymce',
    'newsletter',
    # 'admin_reorder',
    'import_export',
    # testing remove on production
    'django_seed',
    'tracking',
    'report_builder',
    'reversion',


    'core',
    'configuration',
    'authentication.accounts',
    'website',
    'website.blog',
    'website.cms',
    'leads',
    'claims',
    'policies',
    'checkout',
    'payments.mpesa',
    'customer',
    'order',
    'agent',
    'baton.autodiscover',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'tracking.middleware.VisitorTrackingMiddleware',#User tracking
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'customer.middleware.RequestMiddleware',#allow request 
    # 'admin_reorder.middleware.ModelAdminReorder',#admin reoder
]

SITE_ID=1

ROOT_URLCONF = 'elimusmart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',#admin theme
            ],
        },
    },
]

WSGI_APPLICATION = 'elimusmart.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':str(BASE_DIR / 'db.sqlite3'),
    }
}

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

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# accounts
ENABLE_USER_ACTIVATION = False
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = True
LOGIN_VIA_EMAIL_OR_USERNAME = False
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'accounts:log_in'
USE_REMEMBER_ME = True

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = False
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = True

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
TIME_ZONE = 'UTC'
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# ck-editor
CKEDITOR_BASEPATH = "/static/website/ckeditor/"
CKEDITOR_UPLOAD_PATH = "website/ck/"
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
}
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 300,
    },
}
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}
# hijack
HIJACK_ALLOW_GET_REQUESTS = True
# HIJACK_LOGIN_REDIRECT_URL = ''  # Where admins are redirected to after hijacking a user
HIJACK_LOGOUT_REDIRECT_URL = '/admin/auth/user/'  
HijackUserAdmin=False
HIJACK_USE_BOOTSTRAP = True
# crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# mpesa
# The Mpesa environment to use
# Possible values: sandbox, production

MPESA_ENVIRONMENT = 'sandbox'

# Credentials for the daraja app

MPESA_CONSUMER_KEY = 'AqlUwcGc0hhCCZ4mw9bgGEqovUU6deGw'
MPESA_CONSUMER_SECRET = 'eeqwaLYKSlZXcpwT'

#Shortcode to use for transactions. For sandbox  use the Shortcode 1 provided on test credentials page

MPESA_SHORTCODE = '174379'

# Shortcode to use for Lipa na MPESA Online (MPESA Express) transactions
# This is only used on sandbox, do not set this variable in production
# For sandbox use the Lipa na MPESA Online Shorcode provided on test credentials page

MPESA_EXPRESS_SHORTCODE = 'mpesa_express_shortcode'

# Type of shortcode
# Possible values:
# - paybill (For Paybill)
# - till_number (For Buy Goods Till Number)

MPESA_SHORTCODE_TYPE = 'paybill'

# Lipa na MPESA Online passkey
# Sandbox passkey is available on test credentials page
# Production passkey is sent via email once you go live

MPESA_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

# Username for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_USERNAME = 'ElimuSmart'

# Plaintext password for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_SECURITY_CREDENTIAL = 'initiator_security_credential'
# ADMIN_REORDER = (
    #  # Keep original label and models
    # 'sites',
     # Rename app
    # {'app': 'auth', 'label': 'Authorisation'},
 # Cross-linked models
    # {'app': 'auth', 'models': ('auth.User', 'sites.Site')},
#     # First group
#     {'app': 'cms', 'label': 'home',
#      'models': ('cms.HomeCarouselOne',
#                 'cms.HomeCarouselTwo',)
#     },
    # )

# Import export
IMPORT_EXPORT_USE_TRANSACTIONS=True
IMPORT_EXPORT_SKIP_ADMIN_LOG=False
IMPORT_EXPORT_IMPORT_PERMISSION_CODE=1234
IMPORT_EXPORT_EXPORT_PERMISSION_CODE=1234
# newsletter
# Using sorl-thumbnail
NEWSLETTER_THUMBNAIL = 'sorl-thumbnail'
NEWSLETTER_CONFIRM_EMAIL = False
# Using django-tinymce
NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"
# Amount of seconds to wait between each email. Here 100ms is used.
NEWSLETTER_EMAIL_DELAY = 0.1

# Amount of seconds to wait between each batch. Here one minute is used.
NEWSLETTER_BATCH_DELAY = 60

# Number of emails in one batch
NEWSLETTER_BATCH_SIZE = 100
# 
# admin baton
BATON = {
    'SITE_HEADER': 'ELIMUSMART',
    'SITE_TITLE': 'ELIMUSMART',
    'INDEX_TITLE': 'Administration',
    'SUPPORT_HREF': 'https://bismart.co.ke',
    'COPYRIGHT': 'copyright © 2021 <a href="https://www.bismart.co.ke">Bismart</a>', # noqa
    'POWERED_BY': '<a href="https://wwww.bismart.co.ke">Bismart</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Menu',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'LOGIN_SPLASH': '/static/core/img/login-splash.png',
    'SEARCH_FIELD': {
        'label': 'Search contents...',
        'url': '/search/',
    },
    # 'MENU': (
    #     { 'type': 'title', 'label': 'main', 'apps': ('auth', ) },
    #     {
    #         'type': 'app',
    #         'name': 'auth',
    #         'label': 'Authentication',
    #         'icon': 'fa fa-lock',
    #         'models': (
    #             {
    #                 'name': 'user',
    #                 'label': 'Users'
    #             },
    #             {
    #                 'name': 'group',
    #                 'label': 'Groups'
    #             },
    #         )
    #     },
    #     { 'type': 'title', 'label': 'Contents', 'apps': ('flatpages', ) },
    #     { 'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages' },
    #     { 'type': 'free', 'label': 'Custom Link', 'url': 'http://www.google.it', 'perms': ('flatpages.add_flatpage', 'auth.change_user') },
    #     { 'type': 'free', 'label': 'My parent voice', 'default_open': True, 'children': [
    #         { 'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp' },
    #         { 'type': 'free', 'label': 'Another custom link', 'url': 'http://www.google.it' },
    #     ] },
    # ),
    # 'ANALYTICS': {
    #     'CREDENTIALS': os.path.join(BASE_DIR, 'credentials.json'),
    #     'VIEW_ID': '12345678',
    # }
}
# user tracking
TRACK_AJAX_REQUESTS = False
TRACK_ANONYMOUS_USERS = True
TRACK_SUPERUSERS = False
TRACK_PAGEVIEWS = True
TRACK_IGNORE_STATUS_CODES = [400, 404, 403, 405, 410, 500]
TRACK_REFERER = True
TRACK_QUERY_STRING = False

