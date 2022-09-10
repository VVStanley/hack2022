from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.serializers.contracts import (
    ConsumerSerializer, ContractsSerializer,
    SupplierSerializer,
)
from contract.models import Consumer, Contract, Supplier


class SupplierViewSet(RetrieveModelMixin, GenericViewSet):

    lookup_field = 'sup_username'
    permission_classes = (IsAuthenticated,)
    serializer_class = SupplierSerializer

    def get_queryset(self):
        return Supplier.objects.all()


class ConsumerSViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = ConsumerSerializer

    def get_queryset(self):
        if 'sup_username' in self.request.query_params:
            return Consumer.objects.with_sum_contracts().filter(
                consumer_contracts__in=Supplier.objects.get(
                    sup_username=self.request.query_params['sup_username']
                ).my_contracts.all()
            ).order_by('-contract_sum')
        return Consumer.objects.with_sum_contracts().all()

    @action(
        methods=['get'], detail=False, url_path='for-charts'
    )
    def for_charts(self, request):
        data = Consumer.objects.with_sum_contracts().filter(
                consumer_contracts__in=Supplier.objects.get(
                    sup_username=self.request.query_params['sup_username']
                ).my_contracts.all()
            ).order_by(
            '-contract_sum'
        )[:int(self.request.query_params.get('count', 7))]
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContractsSViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = ContractsSerializer

    def get_queryset(self):
        if 'sup_username' in self.request.query_params:
            return Contract.objects.filter(
                id_supplier__sup_username=(
                    self.request.query_params['sup_username']
                )
            )
        return Contract.objects.all()

