from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.newsletter_signup, name='newsletter_signup'),
    re_path(r'^unsubscription/', views.newsletter_unsubscribe, name='unsubscribe'),
]