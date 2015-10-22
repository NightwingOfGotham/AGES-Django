from django.conf.urls import include, url

from angular import urls as angular_urls
from api import urls as api_urls

urlpatterns = [
    url(r'angular/', include(angular_urls)),
    url(r'api/', include(api_urls)),
]
