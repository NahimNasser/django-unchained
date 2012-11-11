from djangorestframework.resources import ModelResource
from basicapi import models as m


class HorseResource(ModelResource):
    model = m.Horse
    fields = ''
