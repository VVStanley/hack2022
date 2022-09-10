from rest_framework.serializers import ModelSerializer

from contract.models import Consumer, Contract, Supplier


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

    class Meta:
        model = Consumer
        fields = (
            'cons_inn',
            'cons_kpp',
            'cons_name',
        )


class ContractsSerializer(ModelSerializer):

    consumer = ConsumerSerializer(read_only=True)

    class Meta:
        model = Contract
        fields = (
            'id_contract',
            'contract',
            'pub_date',
            'contract_date',
            'contract_price',
            'cte',
            'consumer',
        )