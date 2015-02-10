from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
import persons.views as person_views
from system import views as system_view
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crew.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', system_view.index, name='index'),
    url(r'^login/$', system_view.login_view, name='login_view'),
    url(r'^logout/$', system_view.logout_view, name='logout_view'),

    url(r'^home$', system_view.home, name='home'),

    url(r'^persons/', include('persons.urls')),

    )

urlpatterns += patterns('',
                 (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
            )
