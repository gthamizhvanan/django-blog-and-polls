from django.conf.urls import patterns, include, url
from django.contrib import admin
from logmindblog import views

urlpatterns = patterns('',
    # Examples:
    url(r'^polls/',include('polls.urls',namespace="polls"), name="polls"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logmindblog/',include('logmindblog.urls',namespace="logmindblog"), name="logmindblog"),
)
