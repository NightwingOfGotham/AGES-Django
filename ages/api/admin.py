from django.contrib import admin
from models import Fleet, Ship, Officer


class FleetAdmin(admin.ModelAdmin):
	list_display = ['fleet_id', 'name', 'motto']


class ShipAdmin(admin.ModelAdmin):
	list_display = ['ship_id', 'name', 'fleet']


class OfficerAdmin(admin.ModelAdmin):
	list_display = ['officer_id', 'name', 'rank', 'home_planet', 'ship']