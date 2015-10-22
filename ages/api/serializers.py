from django.contrib.auth.models import User, Group
from models import Fleet, Ship, Officer
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['username'])
        user.save()

        for group in validated_data['groups']:
            user.groups.add(group)

        return user

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name',
            'email', 'is_staff', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet
        fields = ('id', 'url', 'name', 'motto')

class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ('id', 'url', 'name', 'fleet')

class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ('id', 'url', 'name', 'rank', 'home_planet', 'ship')

