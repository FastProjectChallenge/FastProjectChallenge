from django.contrib import admin
from .models import BUnit, UnitRelation, UnitRelationChain, UnitRelationChainItem, Comment

admin.site.register(BUnit)
admin.site.register(UnitRelation)
admin.site.register(UnitRelationChain)
admin.site.register(UnitRelationChainItem)
admin.site.register(Comment)