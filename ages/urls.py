from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from angular import urls as angular_urls
from api import urls as api_urls

urlpatterns = [
    url(r'angular/', include(angular_urls)),
    url(r'api/', include(api_urls)),
    url(r'login/$', auth_views.login),
]
