from django.db import models
# Create your models here.
from member.models import Goods
from userinfo.models import UserInfo

ORDERSTATUS = (
        (1, "未支付",),
        (2, "已支付"),
        (3, "订单取消"),
    )


class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo, db_column='user_id', on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, db_column='good_id', on_delete=models.CASCADE)
    ccount = models.IntegerField('数量', db_column='cart_count')

    def __unicode__(self):
        return self.user

    def __str__(self):
        return self.ccount

    class Meta():
        db_table = 'cartinfo'

class Order(models.Model):
    user = models.ForeignKey(UserInfo, db_column='user_id', on_delete=models.CASCADE)
    orderNo= models.CharField("订单号", max_length=200)
    ads= models.CharField("收件人", max_length=200)
    acot= models.CharField("总数", max_length=200)
    acounts= models.CharField("价格", max_length=200)
    cals = models.TextField("orderdetail", null=True, blank=True)
    orderStatus = models.IntegerField("订单状态", blank=True, choices=ORDERSTATUS, default='1')

    def __unicode__(self):
        return self.user

