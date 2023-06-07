from django.contrib import admin
from apps.ad.models import *

admin.site.register(AdModel)
admin.site.register(FavAdModel)
admin.site.register(AdPictureModel)
admin.site.register(SubCategoriesModel)
admin.site.register(CategoriesModel)

