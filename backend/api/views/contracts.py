from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.serializers.contracts import (
    ConsumerSerializer, ContractsSerializer,
    MapSerializer, SupplierSerializer, TruAllSaleConsumersSerializer,
)
from contract.models import Consumer, Contract, Supplier


class SupplierViewSet(RetrieveModelMixin, GenericViewSet):

    lookup_field = 'sup_username'
    permission_classes = (IsAuthenticated,)
    serializer_class = SupplierSerializer

    def get_queryset(self):
        return Supplier.objects.all()


class ConsumersViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if 'sup_username' in self.request.query_params:
            return Consumer.objects.with_sum_contracts().filter(
                consumer_contracts__in=Supplier.objects.get(
                    sup_username=self.request.query_params['sup_username']
                ).my_contracts.all()
            ).order_by('-contract_sum')
        return Consumer.objects.with_sum_contracts().all()

    def get_serializer_class(self):
        actions = {
            'tru_all_consumers_sale': TruAllSaleConsumersSerializer
        }
        return actions.get(self.action, ConsumerSerializer)

    @action(
        methods=['get'], detail=False,
        url_path=r'(?P<id_consumer>[^/.]+)/(?P<sup_username>[^/.]+)'
    )
    def get_data_sale_consumers(self, request, id_consumer=None, sup_username=None):
        supplier = Supplier.objects.get(sup_username=sup_username)
        queryset_data = Consumer.objects.data_sale_consumers(
            id_consumer=id_consumer, id_supplier=supplier.id_sup
        )
        return Response(queryset_data, status=status.HTTP_200_OK)

    @action(
        methods=['get'], detail=False, url_path='for-charts'
    )
    def for_charts(self, request):
        """Данные для построения графика по ТОПУ клиентов"""
        data = Consumer.objects.with_sum_contracts().filter(
                consumer_contracts__in=Supplier.objects.get(
                    sup_username=self.request.query_params['sup_username']
                ).my_contracts.all()
            ).order_by(
            '-contract_sum'
        )[:int(self.request.query_params.get('count', 7))]
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=['get'], detail=False,
        url_path=r'(?P<id_cte>[^/.]+)/all_sale'
    )
    def tru_all_consumers_sale(self, request, id_cte=None):
        """Получаем всех заказчиков по ИД товара"""
        queryset_data = Consumer.objects.tru_all_consumers_sale(
            id_cte=id_cte
        )
        return Response(queryset_data, status=status.HTTP_200_OK)


class ContractsSViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if 'sup_username' in self.request.query_params:
            return Contract.objects.filter(
                id_supplier__sup_username=(
                    self.request.query_params['sup_username']
                )
            )
        return Contract.objects.all()

    def get_serializer_class(self):
        actions = {
            'data_map': MapSerializer
        }
        return actions.get(self.action, ContractsSerializer)

    @action(
        methods=['get'], detail=False,
        url_path='data_map'
    )
    def data_map(self):
        """Данные для отрисовки карты"""
        queryset_data = Contract.objects.data_for_map()
        return Response(queryset_data, status=status.HTTP_200_OK)


