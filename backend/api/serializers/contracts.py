from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer

from contract.models import Consumer, Contract, ContractElement, Supplier


class TruAllSaleConsumersSerializer(Serializer):

    id_consumer = CharField()
    name = CharField()
    quantity = CharField()
    amount = CharField()


class SupplierSerializer(ModelSerializer):
    """Я поставщик"""

    class Meta:
        model = Supplier
        fields = (
            'sup_inn',
            'sup_kpp',
            'sup_name',
            'sup_type',
        )


class SalesDataConsumersSerializer(Serializer):

    id_cte = CharField()
    cte_name = CharField()
    quantity = CharField()
    amount = CharField()
    contracts_cnt = CharField()


class ConsumerSerializer(ModelSerializer):

    contract_sum = SerializerMethodField()

    class Meta:
        model = Consumer
        fields = (
            'id_consumer',
            'contract_sum',
            'cons_inn',
            'cons_kpp',
            'cons_name',
        )

    @staticmethod
    def get_contract_sum(obj):
        return obj.contract_sum if hasattr(obj, 'contract_sum') else '0.0'


class ContractElementsSerializer(ModelSerializer):

    tru_name = SerializerMethodField()
    tru_category = SerializerMethodField()

    class Meta:
        model = ContractElement
        fields = (
            'tru_name',
            'tru_category',
            'id_element',
            'quantity',
            'amount',
            'risk_days',
            'risk_amount',
        )

    @staticmethod
    def get_tru_name(obj):
        return obj.id_cte.cte_name if obj.id_cte else obj.id_cte

    @staticmethod
    def get_tru_category(obj):
        return obj.id_cte.category if obj.id_cte else obj.id_cte


class ContractsSerializer(ModelSerializer):

    elements = ContractElementsSerializer(
        many=True, source='contracts_elements', read_only=True
    )
    consumer = ConsumerSerializer(read_only=True, source='id_consumer')

    class Meta:
        model = Contract
        fields = (
            'id_contract',
            'contract',
            'pub_date',
            'contract_date',
            'contract_price',
            'consumer',
            'elements'
        )


class MapSerializer(Serializer):

    sum_cost = CharField()
    region_name = CharField()
