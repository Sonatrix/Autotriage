"""
autotriage - A Django powered ticket tracker for small enterprise.

templatetags/load_helpdesk_settings.py - returns the settings as defined in
                                    django-helpdesk/helpdesk/settings.py
"""
from __future__ import print_function
from django.template import Library
from autotriage import settings as helpdesk_settings_config


def load_helpdesk_settings(request):
    try:
        return helpdesk_settings_config
    except Exception as e:
        import sys
        print("'autotriage' template tag (autotriage) crashed with following error:",
              file=sys.stderr)
        print(e, file=sys.stderr)
        return ''

register = Library()
register.filter('load_helpdesk_settings', load_helpdesk_settings)
