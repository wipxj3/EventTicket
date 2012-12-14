from django.conf.urls import *
from ticket.views import *

urlpatterns = patterns('',
    # Main web portal entrance.
    (r'^$', ticket_main_page),
)