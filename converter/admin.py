from django.contrib import admin
from .models import PageId, BUnit, UnitRelation, UnitRelationChain, UnitRelationChainItem

admin.site.register(PageId)
admin.site.register(BUnit)
admin.site.register(UnitRelation)
admin.site.register(UnitRelationChain)
admin.site.register(UnitRelationChainItem)