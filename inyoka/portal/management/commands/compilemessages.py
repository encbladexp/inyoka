from subprocess import call

from django.core.management.base import BaseCommand

APPS = ['forum', 'portal', 'wiki', 'ikhaya', 'pastebin', 'planet', 'markup']

class Command(BaseCommand):

    def handle(self, *args, **options):
        for app in APPS:
            call(['pybabel', 'compile', '-D', 'django', '-d',
                  'inyoka/%s/locale' % app, '-l', 'de_DE'])
        # global files
        call(['pybabel', 'compile', '-D', 'django', '-d',
              'inyoka/locale', '-l', 'de_DE'])
