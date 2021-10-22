import graphene

from .models import SellerModel, CustomerModel, BouquetModel, PurchaseModel

from .seller.types import SellerType
from .seller.mutations import CreateSeller, UpdateSeller, DeleteSeller
from .customer.types import CustomerType
from .customer.mutations import CreateCustomer, UpdateCustomer, DeleteCustomer
from .bouquet.types import BouquetType
from .bouquet.mutations import CreateBouquet, UpdateBouquet, DeleteBouquet
from .purchase.types import PurchaseType
from .purchase.mutations import PurchaseBouquet


class Query(graphene.ObjectType):
    seller = graphene.Field(SellerType, id=graphene.Int())
    customer = graphene.Field(CustomerType, id=graphene.Int())
    bouquet = graphene.Field(BouquetType, id=graphene.Int())

    bouquets = graphene.List(BouquetType)
    sellers = graphene.List(SellerType)
    purchases = graphene.List(PurchaseType, customer_id=graphene.ID())

    def resolve_seller(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return SellerModel.objects.get(pk=id)
        return None

    def resolve_customer(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return CustomerModel.objects.get(pk=id)
        return None

    def resolve_bouquet(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return BouquetModel.objects.get(pk=id)
        return None

    def resolve_bouquets(self, info, **kwargs):
        return BouquetModel.objects.all()

    def resolve_sellers(self, info, **kwargs):
        return SellerModel.objects.all()

    def resolve_purchases(self, info, **kwargs):
        id = kwargs.get("customer_id")
        if id is not None:
            return PurchaseModel.objects.filter(customer__id=id)
        return None


class Mutation(graphene.ObjectType):
    create_seller = CreateSeller.Field()
    update_seller = UpdateSeller.Field()
    delete_seller = DeleteSeller.Field()
    create_customer = CreateCustomer.Field()
    update_customer = UpdateCustomer.Field()
    delete_customer = DeleteCustomer.Field()
    create_bouquet = CreateBouquet.Field()
    update_bouquet = UpdateBouquet.Field()
    delete_bouquet = DeleteBouquet.Field()
    purchase_bouquet = PurchaseBouquet.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
