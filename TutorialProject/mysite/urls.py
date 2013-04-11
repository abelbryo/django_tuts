from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from polls import views

urlpatterns = patterns('',

    # For some reason including  polls.urls doesn't work
    # so I added them here
    url(r'^polls/$', views.index, name="index"),
    url(r'^polls/(?P<poll_id>\d+$)', views.detail, name="detail"),
    url(r'^polls/(?P<poll_id>\d+)/result/$', views.result, name="result"),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', views.vote, name="vote"),


    # This doesn't work except for the index page
    # url(r'^polls/$', include('polls.urls')),


    # The admin url
    url(r'^admin/', include(admin.site.urls)),
)
