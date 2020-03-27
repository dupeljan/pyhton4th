from django.db import models

class Meta:
	db_table ='Planets'

# Create your models here.
class SpaceObject(models.Model):
	id = models.AutoField(primary_key =True)
	system_idsystem = models.ForeignKey('SpaceSystem')
	type_idtye = models.ForeignKey('SpaceObjectType')
	name = models.CharField(max_length = 120)
	radius = models.FloatField()
	mass = models.FloatField()

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class SpaceSystem(models.Model):
	id = models.AutoField(primary_key =True)
	name = models.CharField(max_length = 120)
	size = models.FloatField()

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class SpaceObjectType(models.Model):
	id = models.AutoField(primary_key =True)
	name = models.CharField(max_length = 120)
	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name