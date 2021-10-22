import decimal

import graphene

from .types import PurchaseType
from ..models import PurchaseModel, CustomerModel, BouquetModel


class PurchaseBouquet(graphene.Mutation):
    class Arguments:
        customer_id = graphene.ID(required=True)
        bouquet_id = graphene.ID(required=True)

    ok = graphene.Boolean()
    purchase = graphene.Field(PurchaseType)

    @staticmethod
    def mutate(root, info, customer_id, bouquet_id):
        customer = CustomerModel.objects.get(pk=customer_id)
        bouquet = BouquetModel.objects.get(pk=bouquet_id)
        seller = bouquet.seller
        if None in (customer, bouquet, seller):
            return None
        earnings = bouquet.price * decimal.Decimal(0.3)
        seller.sold_bouquets += 1
        purchase = PurchaseModel(
            bouquet=bouquet,
            customer=customer,
            price=bouquet.price,
            earnings=earnings,
        )
        purchase.save()
        seller.save()
        ok = True
        return PurchaseBouquet(purchase=purchase, ok=ok)
