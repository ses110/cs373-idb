from tastypie.resources import ModelResource
from mythos.models import Figure


class MyModelResource(ModelResource):
    class Meta:
        queryset = Figure.objects.all()
        allowed_methods = ['get']
