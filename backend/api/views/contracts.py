from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.serializers.contracts import (
    ConsumerSerializer, ContractsSerializer,
    SupplierSerializer,
)
from contract.models import Consumer, Contract, Supplier


class SupplierViewSet(RetrieveModelMixin, GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = SupplierSerializer

    def get_queryset(self):
        return Supplier.objects.all()


class ConsumerSViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = ConsumerSerializer

    def get_queryset(self):
        return Consumer.objects.all()


class ContractsSViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = ContractsSerializer

    def get_queryset(self):
        return Contract.objects.all()
