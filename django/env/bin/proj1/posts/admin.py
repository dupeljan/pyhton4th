from django.contrib import admin
from .models import SpaceObject, SpaceSystem, SpaceObjectType
# Register your models here.


class SpaceObjectModeAdmin(admin.ModelAdmin):
	list_display = ['name','radius','mass']
	list_display_links = ['name']
	#fields=('title',)
	#exclude = ('likes',)
	class Meta:
		model = SpaceObject

class SpaceObjectTypeModelAdmin(admin.ModelAdmin):
	list_display = ['name']
	class Meta:
		model = SpaceObjectType

class SpaceSystemModelAdmin(admin.ModelAdmin):
	list_display = ['name','size']
	class Meta:
		model = SpaceSystem

admin.site.register(SpaceObject, SpaceObjectModeAdmin)
admin.site.register(SpaceSystem,SpaceSystemModelAdmin)
admin.site.register(SpaceObjectType,SpaceObjectTypeModelAdmin)
