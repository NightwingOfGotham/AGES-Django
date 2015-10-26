from django.db import models

from ages.core.constants import RANKS


class Fleet(models.Model):
    name = models.CharField(max_length=32, unique=True)
    motto = models.CharField(max_length=200)
    fleet_number = models.PositiveIntegerField()

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.motto)


class Ship(models.Model):
    name = models.CharField(max_length=32, unique=True)
    fleet = models.ForeignKey(Fleet)

    def __unicode__(self):
        return u'AGES-%s %s' % (self.pk, self.name)

class Officer(models.Model):
    ADMIRAL = 'ADM'
    FLEET_CAPTAIN = 'FCPT'
    CAPTAIN = 'CAPT'
    COMMANDER = 'CDR'
    LEFTENANT = 'LEF'
    ENSIGN = 'ENS'
    RANK_CHOICES = (
        (RANKS['ADMIRAL']['value'], RANKS['ADMIRAL']['display']),
        (RANKS['FLEET_CAPTAIN']['value'], RANKS['FLEET_CAPTAIN']['display']),
        (RANKS['CAPTAIN']['value'], RANKS['CAPTAIN']['display']),
        (RANKS['COMMANDER']['value'], RANKS['COMMANDER']['display']),
        (RANKS['LEFTENANT']['value'], RANKS['LEFTENANT']['display']),
        (RANKS['ENSIGN']['value'], RANKS['ENSIGN']['display'])
    )

    name = models.CharField(max_length=32, unique=True)
    rank = models.CharField(max_length=4,
                            choices=RANK_CHOICES,
                            default=ENSIGN)
    home_planet = models.CharField(max_length=32)
    ship = models.ForeignKey(Ship)

    def __unicode__(self):
        return u'%s %s' % (self.rank, self.name)


