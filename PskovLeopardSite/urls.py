"""
Definition of urls for PskovLeopardSite.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.views.generic import RedirectView
from django.conf.urls.static import static

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
admin.autodiscover()


urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^tickets$', app.views.tickets, name='tickets'),
    url(r'^roster$', app.views.roster, name='roster'),
    url(r'^timetable$', app.views.timetable, name='timetable'),
    url(r'^links$', app.views.links, name='links'),
    url(r'^pool$', app.views.pool, name='pool'),
    url(r'^stats$', app.views.stats, name='stats'),
    url(r'^registration$', app.views.registration, name= 'registration'),
    url(r'^shop$', app.views.shop, name='shop'),
    url(r'^blog/', app.views.blog, name='blog'),
    url(r'^blogpost/<int:parametr>', app.views.blogpost, name='blogpost'),

    url(r'^newpost', app.views.newpost, name='newpost'),
    url(r'^videopost', app.views.videopost, name='videopost'),

    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Авторизация',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()