from rest_framework import status
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.serializers.tru import TruSerializer, TruSupplierSerializer
from contract.models import Supplier
from tru.models import Tru


class TruViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """Все наименования"""

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Tru.objects.all()

    def get_serializer_class(self):
        actions = {
            'for_supplier': TruSupplierSerializer
        }
        return actions.get(self.action, TruSerializer)

    @action(
        methods=['get'], detail=False,
        url_path=r'(?P<sup_username>[^/.]+)/for-supplier'
    )
    def for_supplier(self, request, sup_username=None):
        supplier = Supplier.objects.get(sup_username=sup_username)
        queryset_data = Tru.objects.get_tru_with_my_sales(
            id_supplier=supplier.id_sup
        )
        page = self.paginate_queryset(queryset_data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(queryset_data, status=status.HTTP_200_OK)
