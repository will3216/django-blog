from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('blog.urls'), name='home'),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
