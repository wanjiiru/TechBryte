from django import template
from django.contrib.sites.models import Site
from django.utils.http import urlquote_plus

register = template.Library()

@register.filter
def google_calendarize(event):


    s = ('http://www.google.com/calendar/event?action=TEMPLATE&' +
         'sprop=website:' + urlquote_plus(Site.objects))
google_calendarize.safe = True
