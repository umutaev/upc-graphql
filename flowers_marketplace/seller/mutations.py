import graphene

from .types import SellerType
from ..models import SellerModel


class CreateSeller(graphene.Mutation):
    class Arguments:
        shop_name = graphene.String(required=True)
        photo_link = graphene.String(required=True)
        creation_date = graphene.Date(required=True)

    ok = graphene.Boolean()
    seller = graphene.Field(SellerType)

    @staticmethod
    def mutate(root, info, shop_name, photo_link, creation_date):
        seller = SellerModel(
            shop_name=shop_name,
            photo_link=photo_link,
            creation_date=creation_date,
        )
        seller.save()
        ok = True
        return CreateSeller(seller=seller, ok=ok)


class UpdateSeller(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        shop_name = graphene.String(required=True)
        photo_link = graphene.String(required=True)
        creation_date = graphene.Date(required=True)

    ok = graphene.Boolean()
    seller = graphene.Field(SellerType)

    @staticmethod
    def mutate(root, info, id, shop_name, photo_link, creation_date):
        seller_instance = SellerModel.objects.get(pk=id)
        if seller_instance is None:
            return UpdateSeller(ok=False, seller=None)
        seller_instance.shop_name = shop_name
        seller_instance.photo_link = photo_link
        seller_instance.creation_date = creation_date
        seller_instance.save()
        ok = True
        return UpdateSeller(ok=ok, seller=seller_instance)


class DeleteSeller(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        seller_instance = SellerModel.objects.get(pk=id)
        if seller_instance is None:
            return DeleteSeller(ok=False)
        seller_instance.delete()
        return DeleteSeller(ok=True)
