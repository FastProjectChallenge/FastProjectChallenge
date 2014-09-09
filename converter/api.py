from .models import PageId, BUnit, UnitRelation, UnitRelationChain, UnitRelationChainItem
from tastypie.resources import ModelResource
from tastypie.api import Api
from django.contrib.auth.models import User
from django.http import HttpResponse

def build_content_type(format, encoding='utf-8'):
    """
    Appends character encoding to the provided format if not already present.
    """
    if 'charset' in format:
        return format

    return "%s; charset=%s" % (format, encoding)

class MyModelResource(ModelResource):
    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        """
        Extracts the common "which-format/serialize/return-response" cycle.

        Mostly a useful shortcut/hook.
        """
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format)
        return response_class(content=serialized, content_type=build_content_type(desired_format), **response_kwargs)

class PageIdResource(MyModelResource):
    class Meta:
        queryset = PageId.objects.all()
        resource_name = 'page'

class UserResource(MyModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_superuser']

class BUnitResource(MyModelResource):
    class Meta:
        queryset = BUnit.objects.all()
        resource_name = 'unit'

class UnitRelationResource(MyModelResource):
    class Meta:
        queryset = UnitRelation.objects.all()
        resource_name = 'relation'

class UnitRelationChainResource(MyModelResource):
    class Meta:
        queryset = UnitRelationChain.objects.all()
        resource_name = 'chain'

class UnitRelationChainItemResource(MyModelResource):
    class Meta:
        queryset = UnitRelationChainItem.objects.all()
        resource_name = 'chain_item'


v1_api = Api(api_name='v1')
v1_api.register(PageIdResource())
v1_api.register(UserResource())
v1_api.register(BUnitResource())
v1_api.register(UnitRelationResource())
v1_api.register(UnitRelationChainResource())
v1_api.register(UnitRelationChainItemResource())


