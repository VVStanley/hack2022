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


class ConsumerSerializer(ModelSerializer):

    contract_sum = SerializerMethodField()

    class Meta:
        model = Consumer
        fields = (
            'contract_sum',
            'cons_inn',
            'cons_kpp',
            'cons_name',
        )

    @staticmethod
    def get_contract_sum(obj):
        return obj.contract_sum if hasattr(obj, 'contract_sum') else '0.0'


class ContractElementsSerializer(ModelSerializer):

    class Meta:
        model = ContractElement
        fields = (
            'id_element',
            'quantity',
            'amount',
        )


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
