from datetime import datetime
from django import get_version
from django.conf import settings
from django.template.defaultfilters import date
from django.utils import timezone

if get_version() < '2.0':
    from django.core.urlresolvers import reverse
else:
    from django.urls import reverse


def url(viewname, *args, **kwargs):
    return reverse(viewname, args=args, kwargs=kwargs)


def now(format_string):
    tzinfo = timezone.get_current_timezone() if settings.USE_TZ else None
    formatted = date(datetime.now(tz=tzinfo), format_string)

    return formatted


def firstof(*args):
    return next((arg for arg in args if bool(arg)), None)
