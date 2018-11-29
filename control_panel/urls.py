from django.conf.urls import re_path
from newsltters.views import control_newsletter


urlpatterns = [
    re_path('newsletter/', control_newsletter, name='control_newsletter'),
]