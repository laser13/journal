from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import DEBUG, MEDIA_ROOT
from django.views.generic import ListView

urlpatterns = patterns('',
    url(r'^$', include('journal.apps.magazine.urls')),
    url(r'^journals/', include('journal.apps.magazine.urls')),
    url(r'^images/image/(?P<image_id>[\d]+)/$', 'journal.apps.magazine.views.image', name='image.show'),
    url(r'^tags/tag/(?P<tag_id>[\d]+)/$', 'journal.apps.magazine.views.tag', name='tag.show'),

    # Uncomment the admin/doc line below to enable admin documentation:
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    )

    urlpatterns += staticfiles_urlpatterns()