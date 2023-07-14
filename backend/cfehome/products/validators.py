from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


# def validated_title(value):
#         qs = Product.objects.filter(title__iexact = value)
#         if qs.exists():
#             raise serializers.ValidationError(f"{value} is already aproduct name")
#         return value

def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} is not Allowed")
    return value

unique_product_title = UniqueValidator(
    queryset=Product.objects.all(),
    lookup= 'iexact'
    )