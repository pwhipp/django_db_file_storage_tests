from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^files/', include('db_file_storage.urls')),
    url(r'^admin/', include(admin.site.urls)))
