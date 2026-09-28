from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discountww = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discountww',
        ]
    
    def get_my_discountww(self, obj):
        return obj.get_discount()