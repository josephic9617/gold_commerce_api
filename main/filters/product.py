import django_filters
from main.models.product import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains", label="Name")
    description = django_filters.CharFilter(field_name="description", lookup_expr="icontains", label="Description")
    price = django_filters.RangeFilter(field_name="price", label="Price")
    weight = django_filters.RangeFilter(field_name="weight", label="Weight")
    created_at = django_filters.DateFromToRangeFilter(field_name="created_at", label="Created at")

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'weight',
            'created_at',
        )