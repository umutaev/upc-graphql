from graphene_django import DjangoObjectType

from ..models import SellerModel


class SellerType(DjangoObjectType):
    class Meta:
        model = SellerModel
        fields = ("id", "shop_name", "photo_link", "creation_date", "sold_bouquets")
