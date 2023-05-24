from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested import UniqueFieldsMixin, NestedUpdateMixin

from platform_app.models import Tag, Product, ProductOption


class TagSerializer(UniqueFieldsMixin, serializers.ModelSerializer) :

    class Meta:
        model = Tag
        fields = ("pk", "name")

class ProductOptionSerializer(serializers.ModelSerializer) :

    class Meta:
        model = ProductOption
        fields = ("pk", "name", "price")        

class ProductSerializer(WritableNestedModelSerializer) :

    option_set = ProductOptionSerializer(many=True)   
    tag_set = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = ("pk", "name", "option_set", "tag_set")
