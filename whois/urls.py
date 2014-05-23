from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from domains.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'whois.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name="domains/index.html")),
)
