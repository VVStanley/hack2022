from rest_framework.fields import (
    CharField, DecimalField,
    SerializerMethodField,
)
from rest_framework.serializers import ModelSerializer, Serializer

from tru.models import Tru, TruDynamics, TruProperty


class TruPropertySerializer(ModelSerializer):

    class Meta:
        model = TruProperty
        fields = (
            'prop_name',
            'prop_value',
            'prop_id',
            'prop_unit',
        )


class TruSerializer(ModelSerializer):

    properties = TruPropertySerializer(many=True, read_only=True)

    class Meta:
        model = Tru
        fields = (
            'id_cte',
            'index',
            'cte_name',
            'category',
            'kpgz_code',
            'characteristics',
            'properties',
            'dynamics',
        )


class TruDynamicsSerializer(Serializer):

    id_cte = CharField()
    contract_year = CharField()
    qty = DecimalField(max_digits=18, decimal_places=6)
    amount = DecimalField(max_digits=18, decimal_places=6)
    price = DecimalField(max_digits=18, decimal_places=6)


class TruSupplierSerializer(Serializer):

    id_cte = CharField()
    dynamics = TruDynamicsSerializer(many=True, read_only=True)

    sum_all = DecimalField(max_digits=18, decimal_places=6)
    my_sum_amount = DecimalField(max_digits=18, decimal_places=6)
    growth_perspective = DecimalField(max_digits=18, decimal_places=6)

    cte_name = CharField()
    category = CharField()
    cons_cnt = CharField()


