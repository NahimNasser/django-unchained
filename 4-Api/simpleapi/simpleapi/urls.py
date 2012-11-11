from django.conf.urls import patterns, include, url
from djangorestframework.views import InstanceModelView, ListOrCreateModelView
from basicapi import resources as rs
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^horses/?$', ListOrCreateModelView.as_view(resource=rs.HorseResource), name='horse_instance'),
    url(r'^horses/(?P<id>\d+)/?$', InstanceModelView.as_view(resource=rs.HorseResource), name='horse_instance'),
    url(r'^restframework', include('djangorestframework.urls', namespace='djangorestframework'))
    # url(r'^simpleapi/', include('simpleapi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
