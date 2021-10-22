from graphene_django import DjangoObjectType

from ..models import CustomerModel


class CustomerType(DjangoObjectType):
    class Meta:
        model = CustomerModel
        fields = ("id", "name", "email")
