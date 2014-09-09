from django.db import models
from django.contrib.auth.models import User
from enum import Enum

class CommentTarget(Enum):
	BUnit = 0
	UnitRelation = 1
	UnitRelationChain = 2

class BUnit(models.Model):
	user = models.ForeignKey(User)

	name = models.CharField(max_length=50)
	short = models.CharField(max_length=5)
	
	description = models.TextField()
	image = models.ImageField(default=None, blank=True, null=True)

	def __str__(self):
		return self.name

class UnitRelation(models.Model):
	user = models.ForeignKey(User)

	sourceUnit = models.ForeignKey(BUnit, related_name='UnitRelation.sourceUnit')
	targetUnit = models.ForeignKey(BUnit, related_name='UnitRelation.targetUnit')

	name = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(default=None, blank=True, null=True)

	coefficient = models.FloatField(default=1)

	like = models.IntegerField(default=0)
	dislike = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class UnitRelationChain(models.Model):
	sourceUnit = models.ForeignKey(BUnit, related_name='sourceUnit')
	targetUnit = models.ForeignKey(BUnit, related_name='targetUnit')

	name = models.CharField(max_length=50)

	coefficient = models.FloatField(default=1)

	like = models.IntegerField(default=0)
	dislike = models.IntegerField(default=0)

class UnitRelationChainItem(models.Model):
	relation = models.ForeignKey(UnitRelation)
	chain = models.ForeignKey(UnitRelationChain)
	position = models.IntegerField(default=0)

class Comment(models.Model):
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	
	content = models.TextField()
	image = models.ImageField(default=None, blank=True, null=True)

	relateTo = models.ForeignKey("self", default=None, blank=True, null=True)

	like = models.IntegerField(default=0)
	dislike = models.IntegerField(default=0)

	target = models.IntegerField(default=0)
	unit = models.ForeignKey(BUnit, default=None, blank=True, null=True)
	relation = models.ForeignKey(UnitRelation, default=None, blank=True, null=True)
	chain = models.ForeignKey(UnitRelationChain, default=None, blank=True, null=True)

	