from django.db import models


class SellerModel(models.Model):
    shop_name = models.CharField(max_length=256)
    photo_link = models.URLField()
    creation_date = models.DateField()
    sold_bouquets = models.IntegerField(default=0)


class CustomerModel(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()


class BouquetModel(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    photo_link = models.URLField()
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE)


class PurchaseModel(models.Model):
    bouquet = models.ForeignKey(BouquetModel, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    earnings = models.DecimalField(max_digits=9, decimal_places=2)
