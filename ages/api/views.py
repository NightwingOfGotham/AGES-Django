from django.contrib.auth.models import User, Group
from models import Fleet, Ship, Officer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from serializers import UserSerializer, GroupSerializer
from serializers import FleetSerializer, ShipSerializer, OfficerSerializer

# for custom GET of available menu list
from rest_framework import generics

# for custom GET of available menu details
from rest_framework.exceptions import APIException


class ForbiddenAccess(APIException):
    status_code = 403
    default_detail = 'Action Forbidden'


class FleetShipList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ShipSerializer

    def get_queryset(self):
        fleet = self.kwargs['fleet']
        return Ship.objects.filter(fleet=fleet)


class ShipOfficerList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = OfficerSerializer

    def get_queryset(self):
        ship = self.kwargs['ship']
        return Officer.objects.filter(ship=ship)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FleetViewSet(viewsets.ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer


class ShipViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class OfficerViewSet(viewsets.ModelViewSet):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer


def create_user(request):
    ## turn this into a class with a GET for form render and a POST for user creation
    pass