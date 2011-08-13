# -*- coding: utf-8 -*-
"""
    inyoka.default_settings
    ~~~~~~~~~~~~~~~~~~~~~~~

    The inyoka default settings.

    :copyright: (c) 2007-2011 by the Inyoka Team, see AUTHORS for more details.
    :license: GNU GPL, see LICENSE for more details.
"""
from os.path import dirname, join
from django.conf.global_settings import *

#: Base path of this application
BASE_PATH = dirname(__file__)

#: Disable all debugging by default
DEBUG = False
DEBUG_NOTIFICATIONS = False
DEBUG_PROPAGATE_EXCEPTIONS = False

# per default there are no managers and admins.  I guess that's
# unused :)
MANAGERS = ADMINS = ()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# the setting here has nothing to do with the timezone the user is
#
# We set the TIME_ZONE to `None` on default so that Django does not
# issue time zone aware columns on postgresql.  This finally should fix
# the last standing bugs regarding postgresql. --entequak
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
LANGUAGE_CODE = 'de-de'
LOCALE_PATHS = ('locale',)

# the base url (without subdomain)
BASE_DOMAIN_NAME = 'ubuntuusers.de'
SESSION_COOKIE_DOMAIN = '.%s' % BASE_DOMAIN_NAME.split(':')[0]

# this url conf is used for contrib stuff like the auth system
ROOT_URLCONF = 'inyoka.portal.urls'
# host conf for subdomain dispatching
ROOT_HOSTCONF = 'inyoka.hosts'
DEFAULT_HOST = 'portal'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

# Absolute path to the directory that holds media and the URL
MEDIA_ROOT = join(BASE_PATH, 'media')
MEDIA_URL = 'http://media.%s' % BASE_DOMAIN_NAME

# same for static
STATIC_ROOT = join(BASE_PATH, 'static-collected')
STATIC_URL = 'http://static.%s' % BASE_DOMAIN_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + '/_admin/'

STATICFILES_DIRS = (
    join(BASE_PATH, 'static'),
)

# system settings
INYOKA_SYSTEM_USER = u'ubuntuusers.de'
INYOKA_SYSTEM_USER_EMAIL = '@'.join(['system', BASE_DOMAIN_NAME])
INYOKA_ANONYMOUS_USER = u'anonymous'
INYOKA_CONTACT_EMAIL = '@'.join(['contact', BASE_DOMAIN_NAME])

# logger name for remote exception logging
INYOKA_LOGGER_NAME = u'inyoka'

# use etags
USE_ETAGS = True

# prefix for the system mails
EMAIL_SUBJECT_PREFIX = u'ubuntuusers: '

EMAIL_BACKEND = 'inyoka.utils.mail.SendmailEmailBackend'

# path to the xapian database
# Examples: /path/to/inyoka.xapdb, or tcpsrv://localhost:3000/
XAPIAN_DATABASE = join(BASE_PATH, 'inyoka.xapdb')

# imagemagick path. leave empty for auto detection
IMAGEMAGICK_PATH = ''

# forum settings
FORUM_LIMIT_UNREAD = 100
FORUM_THUMBNAIL_SIZE = (64, 64)
# time in seconds after posting a user is allowed to edit/delete his own posts,
# for posts (without, with) replies. -1 for infinitely, 0 for never
FORUM_OWNPOST_EDIT_LIMIT = (-1, 1800)
FORUM_OWNPOST_DELETE_LIMIT = (0, 0)

# the id of the ikhaya team group
IKHAYA_GROUP_ID = 1

# settings for the jabber bot
JABBER_BOT_SERVER = '127.0.0.1:6203'

# hours for a user to activate the account
ACTIVATION_HOURS = 48

# days to describe an inactive user
USER_INACTIVE_DAYS = 365

# key for google maps
GOOGLE_MAPS_APIKEY = ''

# wiki settings
WIKI_MAIN_PAGE = 'Startseite'

# The forum that should contain the wiki discussions
WIKI_DISCUSSION_FORUM = 'diskussionen'

# the page below we have our templates.  The template the
# user specifies in the macro or in the parser is then
# joined with this page name according to our weird joining
# rules
WIKI_TEMPLATE_BASE = 'Wiki/Vorlagen'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b)l0ju3erxs)od$g&l_0i1za^l+2dwgxuay(nwv$q4^*c#tdwt'

# a prefix that is automatically added on every cache operation to the key.
# You won't notice anything of it at all but it makes it possible to run more
# than one application on a single memcached server without the risk of cache
# key collision.
CACHE_PREFIX = 'ubuntu_de/'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'KEY_PREFIX': CACHE_PREFIX,
    },
    'request': {
        'BACKEND': 'inyoka.utils.cache.RequestCache',
    }
}


AVAILABLE_FEED_COUNTS = {
    None: (10, 25),
    'ikhaya_feed_article': (10, 20, 25),
    'ikhaya_feed_comment': (10, 20, 25),
    'forum_topic_feed': (10, 20, 25, 50),
    'forum_forum_feed': (10, 20, 25, 50, 75, 100),
    'planet_feed': (10, 20, 25, 50),
    'wiki_feed': (10, 20),
}

MIDDLEWARE_CLASSES = (
    'inyoka.middlewares.common.CommonServicesMiddleware',
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'inyoka.middlewares.session.AdvancedSessionMiddleware',
    'inyoka.middlewares.auth.AuthMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'inyoka.middlewares.services.ServiceMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'inyoka.middlewares.highlighter.HighlighterMiddleware',
    'inyoka.middlewares.security.SecurityMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)

#: We only allow uploads via memory up to 2.5mb and do not stream into
#: temporary files.
FILE_UPLOAD_HANDLERS = ('django.core.files.uploadhandler.MemoryFileUploadHandler',)

TEMPLATE_DIRS = (
    join(BASE_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'inyoka.portal',
    'inyoka.wiki',
    'inyoka.forum',
    'inyoka.ikhaya',
    'inyoka.pastebin',
    'inyoka.planet',
    'django_openid',
    'sentry.client',
    'south',
    # *must* be installed after south
    'django_nose',
    'djcelery',
    'djkombu',
#    'debug_toolbar',
    'django_mobile',
    'django_hosts',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# don't use migrations but just syncdb
SOUTH_TESTS_MIGRATE = False

OPENID_PROVIDERS = {
#    'myopenid': {
#        'name': 'MyOpenID',
#        'url': 'http://{username}.myopenid.com/'
#    },
    'openid': {
      'name': 'OpenID',
      'url': None
    },
    'launchpad': {
        'name': 'Launchpad',
        'url': 'https://launchpad.net/~{username}'
    },
    'claimid': {
      'name': 'ClaimID',
      'url': 'http://claimid.com/{username}'
    },
    'google': {
      'name': 'Google',
      'url': 'https://www.google.com/accounts/o8/id'
    }
}

# some terms to exclude by default to maintain readability
SEARCH_DEFAULT_EXCLUDE = ['Cstammtisch']

# Default blocksize to delmit queries to the search index
SEARCH_INDEX_BLOCKSIZE = 5000

# Set the default sentry site
SENTRY_SITE = "ubuntuusers.de"


# Import and activate django-celery support
import djcelery
djcelery.setup_loader()

# Celery broker preferences.
# http://celeryq.org/docs/configuration.html#celery-result-backend
CELERY_RESULT_BACKEND = 'database'

# SQLAlchemy compatible uri.
# NOTE: This is some kind of deactivated since we are using
# django-celery for this stuff.
CELERY_RESULT_DBURI = 'sqlite://'

# Modules that hold task definitions
CELERY_IMPORTS = [
    'inyoka.tasks',
    'inyoka.wiki.tasks',
]

CELERY_SEND_TASK_ERROR_EMAILS = False
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_EAGER_PROPAGATES_EXCEPTIONS = False
CELERY_ALWAYS_EAGER = DEBUG

# Do not hijack the root logger, avoids unicode errors
CELERYD_HIJACK_ROOT_LOGGER = False

# http://ask.github.com/kombu/introduction.html#transport-comparison
BROKER_BACKEND = 'inyoka.utils.celery_support.DatabaseTransport'

BROKER_HOST = 'localhost'
BROKER_PORT = 5672
BROKER_USER = ''
BROKER_PASSWORD = ''
BROKER_VHOST = ''

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
#    'debug_toolbar.panels.cache.CacheDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

INTERNAL_IPS = ('127.0.0.1',)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
}

# export only uppercase keys
__all__ = list(x for x in locals() if x.isupper())
