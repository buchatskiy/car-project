from django.conf.urls import patterns, include, url
from django.contrib import admin
from models.views import cart

urlpatterns = patterns('',
    url(r'^$', cart),
    url(r'^admin/', include(admin.site.urls)),
)
