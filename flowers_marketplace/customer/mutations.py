import graphene

from .types import CustomerType
from ..models import CustomerModel


class CreateCustomer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    ok = graphene.Boolean()
    customer = graphene.Field(CustomerType)

    @staticmethod
    def mutate(root, info, name, email):
        customer = CustomerModel(name=name, email=email)
        customer.save()
        ok = True
        return CreateCustomer(customer=customer, ok=ok)


class UpdateCustomer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    ok = graphene.Boolean()
    customer = graphene.Field(CustomerType)

    @staticmethod
    def mutate(root, info, id, name, email):
        customer_instance = CustomerModel.objects.get(pk=id)
        if customer_instance is None:
            return UpdateCustomer(ok=False, customer=None)
        customer_instance.name = name
        customer_instance.email = email
        customer_instance.save()
        ok = True
        return UpdateCustomer(ok=ok, customer=customer_instance)


class DeleteCustomer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        customer_instance = CustomerModel.objects.get(pk=id)
        if customer_instance is None:
            return DeleteCustomer(ok=False)
        customer_instance.delete()
        return DeleteCustomer(ok=True)
