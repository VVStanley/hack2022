from rest_framework.serializers import ModelSerializer

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


class TruDynamicsSerializer(ModelSerializer):

    class Meta:
        model = TruDynamics
        fields = (
            'dynamics',
        )


class TruSerializer(ModelSerializer):

    tru_dynamics = TruDynamicsSerializer(
        many=True, read_only=True, source='dynamics'
    )
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
            'tru_dynamics',
        )
