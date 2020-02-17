from api.models import Book
from rest_framework import serializers
from decimal import Decimal
from django.db import models


class Book(models.Model):
    """本モデル"""
    class Meta:
        db_table = 'book'
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        title = models.CharField(verbose_name='タイトル', max_length=20)


 TAX_RATE = 0.1

 class BookSerializer(serializers.ModelSerializer):
     """本モデル⽤シリアライザ"""  price_with_tax = serializers.SerializerMethodField()  # 追加
     class Meta:  
        model = Book  
        fields = ['id', 'title', 'price', 'price_with_tax']  # 修正

    def get_price_with_tax(self, instance):  # 追加
        if instance.price is None:
                return None
        return int(Decimal(instance.price) * Decimal(1 + TAX_RATE)) 
