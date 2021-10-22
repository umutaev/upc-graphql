from graphene_django import DjangoObjectType

from ..models import BouquetModel


class BouquetType(DjangoObjectType):
    class Meta:
        model = BouquetModel
        fields = ("id", "name", "price", "photo_link", "seller")
