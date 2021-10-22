from graphene_django import DjangoObjectType

from ..models import PurchaseModel


class PurchaseType(DjangoObjectType):
    class Meta:
        model = PurchaseModel
        fields = ("id", "bouquet", "customer", "price", "earnings")
