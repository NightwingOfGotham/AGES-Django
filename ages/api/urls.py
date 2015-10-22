from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from views import UserViewSet, GroupViewSet
from views import (
    FleetViewSet,
    OfficerViewSet,
    ShipViewSet,
)
from views import (
    FleetShipList,
    ShipOfficerList,
)

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'fleet', FleetViewSet)
router.register(r'officer', OfficerViewSet)
router.register(r'ship', ShipViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'admin/', include(admin.site.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'fleet-ships/(?P<fleet_pk>[0-9]+)/$', FleetShipList.as_view()),
    url(r'ship-officers/(?P<ship_pk>[0-9]+)/$', ShipOfficerList.as_view()),
]