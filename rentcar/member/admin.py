from django.contrib import admin
from .models import GoodsType, Goods
# Register your models here.
admin.site.register(Goods)
admin.site.register(GoodsType)