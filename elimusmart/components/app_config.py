from decouple import config
# accounts
ENABLE_USER_ACTIVATION = True
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = True
LOGIN_VIA_EMAIL_OR_USERNAME = False
LOGIN_REDIRECT_URL = 'customer_account'
LOGIN_URL = 'accounts:log_in'
USE_REMEMBER_ME = True

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = True
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = True

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
    'LOGIN_SPLASH': 'https://as1.ftcdn.net/jpg/02/51/15/48/500_F_251154835_9Iafmou4CSZ4K6kcfi63eDUlLQo0Gc9F.jpg',
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
# Email communication
SENDGRID_API_KEY=config('SENDGRID_API_KEY')
