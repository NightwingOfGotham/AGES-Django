from django.conf.urls import url
from django.contrib import admin

from ages.angular.views import (
    main,
    new_user,
)

admin.autodiscover()

urlpatterns = [
    url(r'^$', main, name='main'),
]