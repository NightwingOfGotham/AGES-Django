from django.contrib.auth.models import User, Group
from django.shortcuts import render
from models import Fleet, Ship, Officer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from serializers import UserSerializer, GroupSerializer
from serializers import FleetSerializer, ShipSerializer, OfficerSerializer

# for custom GET of available menu list
from rest_framework import mixins
from rest_framework import generics

# for custom GET of available menu details
from django.http import Http404
from rest_framework.exceptions import APIException
from rest_framework.response import Response 
from rest_framework.views import APIView 


class ForbiddenAccess(APIException):
    status_code = 403
    default_detail = 'Action Forbidden'


class FleetShipList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_class = ()
    queryset = Ship.objects.filter(fleet=fleet_pk)
    serializer_class = ShipSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ShipOfficerList(APIView):
    permission_class = ()

    def get_objects(self, pk):
        try:
            return Officer.objects.get(pk=pk)
        except Officer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        officers = self.get_objects(pk)
        serializer = OfficerSerializer(officers, context={'request':request})
        return Response(serializer.data)


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