from django.db import models
from django.contrib.auth.models import User
from enum import Enum

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['get'] = reverse
    return type('Enum', (), enums)

PageType = enum('Unit', 'Relation', 'Chain')

class PageId(models.Model):
	target = models.IntegerField(default=0)	
	def __str__(self):
		return "Page " + str(self.id) + "  " + PageType.get[self.target]

class BUnit(models.Model):
	page = models.OneToOneField(PageId, null=True)
	name = models.CharField(max_length=50)
	user = models.IntegerField(default=0)
	short = models.CharField(max_length=5)
	description = models.TextField()
	image = models.ImageField(default=None, blank=True, null=True)
	def __str__(self):
		return self.name

class UnitRelation(models.Model):
	page = models.OneToOneField(PageId, null=True)
	name = models.CharField(max_length=50)
	user = models.IntegerField(default=0)
	sourceUnit = models.ForeignKey(BUnit, related_name='UnitRelation.sourceUnit')
	targetUnit = models.ForeignKey(BUnit, related_name='UnitRelation.targetUnit')
	description = models.TextField()
	image = models.ImageField(default=None, blank=True, null=True)
	coefficient = models.FloatField(default=1)
	def __str__(self):
		return self.name

class UnitRelationChain(models.Model):
	page = models.OneToOneField(PageId, null=True)
	name = models.CharField(max_length=50)
	sourceUnit = models.ForeignKey(BUnit, related_name='sourceUnit')
	targetUnit = models.ForeignKey(BUnit, related_name='targetUnit')
	coefficient = models.FloatField(default=1)
	def __str__(self):
		return self.name

class UnitRelationChainItem(models.Model):
	position = models.IntegerField(default=0)
	chain = models.ForeignKey(UnitRelationChain)
	relation = models.ForeignKey(UnitRelation)

