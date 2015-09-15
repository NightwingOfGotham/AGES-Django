from django.db import models


class Fleet(models.Model):
    name = models.CharField(max_length=32, unique=True)
    motto = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.motto)


class Ship(models.Model):
    name = models.CharField(max_length=32, unique=True)
    fleet = models.ForeignKey(Fleet)

    def __unicode__(self):
        return u'AGES-%s %s' % (self.pk, self.name)

class Officer(models.Model):
    ADMIRAL = 'ADM'
    CAPTAIN = 'CAPT'
    COMMANDER = 'CDR'
    LEFTENANT = 'LEF'
    ENSIGN = 'ENS'
    RANK_CHOICES = (
        (ADMIRAL, 'Admiral'),
        (CAPTAIN, 'Captain'),
        (COMMANDER, 'Commander'),
        (LEFTENANT, 'Leftenant'),
        (ENSIGN, 'Ensign')
    )

    name = models.CharField(max_length=32, unique=True)
    rank = models.CharField(max_length=4,
                            choices=RANK_CHOICES,
                            default=ENSIGN)
    home_planet = models.CharField(max_length=32)
    ship = models.ForeignKey(Ship)

    def __unicode__(self):
        return u'%s %s' % (self.rank, self.name)


