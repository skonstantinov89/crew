from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from persons.views import SetOperations

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crew.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'new$', SetOperations.newPerson.as_view()),

    )
print(urlpatterns)