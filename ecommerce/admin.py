from django.contrib import admin
from .models import UserAddress,User,Product,ProductBrand,ProductCategory,ProductReview
# Register your models here.

admin.site.register(UserAddress)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(ProductCategory)
admin.site.register(ProductBrand)



