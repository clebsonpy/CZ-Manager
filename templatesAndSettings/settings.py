"""
Keep this file untracked
"""
import os

# ========================================================================
# ACTUAL SETTINGS ========================================================
APP_NAME = "ODM2CZOData" # This has to match the name of the folder that the app is saved
VERBOSE_NAME = "ODM2CZOData"

SITE_HEADER = "ODM2 Admin"
SITE_TITLE = "ODM2 Admin"

ROOT = 'C:/Users/leonmi/Google Drive/ODM2Djangoadmin'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
templates_dir = os.path.dirname(__file__)
# TEMPLATE_DIR_APP = os.path.join(os.path.dirname(__file__), '..')
templates_path = os.path.join(templates_dir, 'templates')
# TEMPLATE_PATH2 = os.path.join(TEMPLATE_DIR, 'templates/odm2testapp')
# print(TEMPLATE_PATH)
templates_dirs = [templates_path, ]  # TEMPLATE_PATH2,

EMAIL_HOST = 'smtp.host'
EMAIL_HOST_USER = 'user'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_FROM_ADDRESS = 'do-not-reply-ODM2-Admin@cuahsi.org'
RECAPTCHA_PUBLIC_KEY = 'googlerecaptchakey'
RECAPTCHA_PRIVATE_KEY = 'googlerecaptchaprivatekey'
EMAIL_USE_TLS = True
EMAIL_PORT = 123

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': templates_dirs,
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]
# TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'random_secret_key_like_so_7472873649836'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TEMPLATE_DEBUG = template_debug
ADMINS = [{"name": "first last",
           "email": "email@example.com"
           }]
ALLOWED_HOSTS = []

MEDIA_ROOT = '{}'.format(ROOT)
MEDIA_URL = '/odm2testapp/upfiles/'
# Application definition
CUSTOM_TEMPLATE_PATH = '/admin/{}/'.format(APP_NAME)
# ADMIN_SHORTCUTS_PATH=admin_shortcuts_path
URL_PATH = 'admin/'
STATIC_ROOT = '{}/static'.format(ROOT)
MAP_CONFIG = {
    "lat": 0,
    "lon": 0,
    "zoom": 2,
    # MapBox
    "MapBox": {
        "access_token": 'mapbox accessToken'
    },
    # should sampling features of type site be added to marker clusters or not
    "cluster_sites": False,
    # how many months by default should time series generated from the map display
    "time_series_months": 3,
}
DATA_DISCLAIMER = {
    "text": "Add a link discribing where your data come from ",
    "linktext": "The name of my site",
    "link": "http://mysiteswegpage.page/",

}
# https://github.com/mishbahr/django-modeladmin-reorder
# {'app': 'auth', 'models': ('auth.User', 'auth.Group')},
# ADMIN_REORDER = ('odm2testsite',
#                  {'app':'Odm2Testapp',
#                   'auth':'staff',
#                   'models':("People", "Organizations","Affiliations", "Variables","Units",
#                       "Taxonomicclassifiers","Methods","Actions","Relatedactions","Actionby","Samplingfeatures",
#                       "Featureactions","Datatsets","Results","Datasetsresults","Processinglevels","Measurementresults",
#                       "Measurementresultvalues","MeasurementresultvalueFile", "Dataloggerfiles",
#                       "Dataloggerprogramfiles")},
# )
INSTALLED_APPS = (
    'jquery',
    'djangocms_admin_style',
    '{}'.format(APP_NAME),
    'import_export',
    'admin_shortcuts',
    'daterange_filter',
    # 'dal',
    # 'dal_select2',
    'ajax_select',
    'django.contrib.admin',
    'django.contrib.gis',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'admin_reorder',

)
# TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#    'apptemplates.Loader',
# )
# find icon images here https://github.com/alesdotio/
# django-admin-shortcuts/blob/master/admin_shortcuts/
# templatetags/admin_shortcuts_tags.py#L134
ADMIN_SHORTCUTS = [
    {

        'shortcuts': [
            {
                'url': CUSTOM_TEMPLATE_PATH,
                'app_name': '{}'.format(APP_NAME),
                'title': '{} Admin'.format(VERBOSE_NAME),
                'class': 'config',
            },
            {
                'url': '/' + URL_PATH + 'AddSensor.html',
                'app_name': '{}'.format(APP_NAME),
                'title': 'Add Sensor Data',
                'class': 'tool',
            },
            {
                'url': '/' + URL_PATH + 'AddProfile.html',
                'app_name': '{}'.format(APP_NAME),
                'title': 'Add Soil Profile Data',
                'class': 'flag',
            },
            {
                'url': '/' + URL_PATH + 'RecordAction.html',
                'app_name': '{}'.format(APP_NAME),
                'title': 'Record an Action',
                'class': 'notepad',
            },
            {
                'url': '/' + URL_PATH + 'ManageCitations.html',
                'app_name': '{}'.format(APP_NAME),
                'title': 'Manage Citations',
                'class': 'pencil',
            },
            {
                'url': '/' + URL_PATH + 'chartIndex.html',
                'app_name': '{}'.format(APP_NAME),
                'title': 'Graph My Data',
                'class': 'monitor',
            },
        ]
    },
]
ADMIN_SHORTCUTS_SETTINGS = {
    'hide_app_list': False,
    'open_new_window': False,
}

# https://github.com/crucialfelix/django-ajax-selects
AJAX_LOOKUP_CHANNELS = dict(
    cv_variable_name=('{}.lookups'.format(APP_NAME), 'CvVariableNameLookup'),
    cv_variable_type=('{}.lookups'.format(APP_NAME), 'CvVariableTypeLookup'),
    cv_unit_type=('{}.lookups'.format(APP_NAME), 'CvUnitTypeLookup'),
    cv_speciation=('{}.lookups'.format(APP_NAME), 'CvVariableSpeciationLookup'),
    featureaction_lookup=('{}.lookups'.format(APP_NAME), 'FeatureactionsLookup'),
    result_lookup=('{}.lookups'.format(APP_NAME), 'ResultsLookup'),
    profileresult_lookup=('{}.lookups'.format(APP_NAME), 'ProfileResultsLookup'),
    measurementresult_lookup=('{}.lookups'.format(APP_NAME), 'MeasurementResultsLookup'),
    timeseriesresult_lookup=('{}.lookups'.format(APP_NAME), 'TimeseriesResultsLookup'),
    cv_taxonomic_classifier_type=('{}.lookups'.format(APP_NAME), 'CvTaxonomicClassifierTypeLookup'),
    cv_method_type=('{}.lookups'.format(APP_NAME), 'CvMethodTypeLookup'),
    cv_action_type=('{}.lookups'.format(APP_NAME), 'CvActionTypeLookup'),
    cv_sampling_feature_type=('{}.lookups'.format(APP_NAME), 'CvSamplingFeatureTypeLookup'),
    cv_sampling_feature_geo_type=('{}.lookups'.format(APP_NAME), 'CvSamplingFeatureGeoTypeLookup'),
    cv_elevation_datum=('{}.lookups'.format(APP_NAME), 'CvElevationDatumLookup'))

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware', didn't work in production
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'admin_reorder.middleware.ModelAdminReorder',
)

ROOT_URLCONF = 'templatesAndSettings.urls'

WSGI_APPLICATION = 'templatesAndSettings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'odm2',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'options': '-c search_path=admin,odm2,odm2extra'
        }
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
# =======================================================
