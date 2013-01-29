from django.conf.urls import patterns, include, url
from django_site_users.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    # Web portal.
    (r'^ticket/', include('ticket.urls')),
    # Examples:
    # url(r'^$', 'EventTicket.views.home', name='home'),
    # url(r'^EventTicket/', include('EventTicket.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
    (r'^register/', 'ticket.views.register_view'),

    url(r'^email-notification/add/', 'ticket.views.email_notification_add', name='AddEmailNotification'),
    url(r'^email-notification/', 'ticket.views.email_notification_list', name="ListEmailNotifications"),
)
