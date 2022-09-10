from rest_framework.serializers import ModelSerializer

from tru.models import Tru, TruProperty


class DataTruPropertySerializer(ModelSerializer):

    class Meta:
        model = TruProperty
        fields = (
            'prop_name',
            'prop_value',
            'prop_id',
            'prop_unit',
        )


class DataTruSerializer(ModelSerializer):

    properties = DataTruPropertySerializer(
        many=True, read_only=True
    )

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
        )
