import graphene

from .types import BouquetType
from ..models import BouquetModel, SellerModel


class CreateBouquet(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Decimal(required=True)
        photo_link = graphene.String(required=True)
        seller_id = graphene.Int(required=True)

    ok = graphene.Boolean()
    bouquet = graphene.Field(BouquetType)

    @staticmethod
    def mutate(root, info, name, price, photo_link, seller_id):
        seller = SellerModel.objects.get(pk=seller_id)
        if seller is None:
            return CreateBouquet(bouquet=None, ok=False)
        bouquet = BouquetModel(
            name=name, price=price, photo_link=photo_link, seller=seller
        )
        bouquet.save()
        ok = True
        return CreateBouquet(bouquet=bouquet, ok=ok)


class UpdateBouquet(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Decimal(required=True)
        photo_link = graphene.String(required=True)
        seller_id = graphene.Int(required=True)

    ok = graphene.Boolean()
    bouquet = graphene.Field(BouquetType)

    @staticmethod
    def mutate(root, info, id, name, price, photo_link, seller_id):
        bouquet_instance = BouquetModel.objects.get(pk=id)
        if bouquet_instance is None:
            return UpdateBouquet(ok=False, bouquet=None)
        seller = SellerModel.objects.get(pk=seller_id)
        if seller is None:
            return UpdateBouquet(ok=False, bouquet=None)
        bouquet_instance.name = name
        bouquet_instance.price = price
        bouquet_instance.photo_link = photo_link
        bouquet_instance.seller = seller
        bouquet_instance.save()
        ok = True
        return UpdateBouquet(ok=ok, bouquet=bouquet_instance)


class DeleteBouquet(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        bouquet_instance = BouquetModel.objects.get(pk=id)
        if bouquet_instance is None:
            return DeleteBouquet(ok=False)
        bouquet_instance.delete()
        return DeleteBouquet(ok=True)
