from django.contrib import admin
from .models import BouquetModel, PurchaseModel, SellerModel, CustomerModel

admin.site.register(BouquetModel)
admin.site.register(PurchaseModel)
admin.site.register(SellerModel)
admin.site.register(CustomerModel)
