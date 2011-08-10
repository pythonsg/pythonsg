import os

# ================
# django settings
# ================

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'
LANGUAGES = (('en', 'English'),)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

PROJECT_ROOT = os.path.dirname(__file__)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(os.path.abspath(
    os.path.join(PROJECT_ROOT, '..', 'proj_public', 'media')), '')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(os.path.abspath(
    os.path.join(PROJECT_ROOT, '..', 'proj_public', 'static')), '')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths
    os.path.join(os.path.abspath(
        os.path.join(PROJECT_ROOT, '..', 'proj_public', 'static', 'pythonsg')), ''),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody. 
# Place a SECRET_KEY in your local_settings.py
# SECRET_KEY = 'generate your key here: http://www.miniwebtool.com/django-secret-key-generator/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
    #'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'proj.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), 'templates'),
)

# ====================
# django-cms settings
# ====================
CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
)
CMS_LANGUAGES = (
    ('en', 'English'),
)
CMS_SEO_FIELDS = True
CMS_REDIRECTS = True

# ========================
# cmsplugin-blog settings
# ========================
CMSPLUGIN_BLOG_PLACEHOLDERS = ('content',)
JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'

# ==================================
# cmsplugin-blog-paginated settings
# ==================================
BLOG_PAGINATE_BY = 15

# =========================
# easy-thumbnails settings
# =========================
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    #'django.contrib.gis',
    # django-cms related apps
    'cms',
    'cms.plugins.text',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'cms.plugins.inherit',
    'mptt',
    'publisher',
    'menus',
    'sekizai',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    # cmsplugin-blog related apps
    'cmsplugin_blog',
    'djangocms_utils',
    'simple_translation',
    'tagging',
    'cmsplugin_blog_paginated',
    # useful 3rd party apps
    'south',
    'easy_thumbnails',
    'filer',
    # our own apps
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',

    # Enable the request object in templates
    'django.core.context_processors.request',

    'django.contrib.messages.context_processors.messages',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# set the env var because we're going to import modules that might do 'from django.conf import settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'proj.settings'

#####
# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
# If you would like to have your own Database Server installed on your local machine,
# Use the local_settings.py file to add in your specific DATABASE settings. (e.g. DATABASE_HOST = '')
# The local_settings.py file is ignored by git so when you push, it will not be pushed into the remote repo.
#####

# use execfile so we can append to existing variables instead of overwriting them
locset = os.path.join(os.path.dirname(__file__), 'local_settings.py')
if os.path.exists(locset):
    execfile(locset)
