from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.serializers.tru import TruSerializer
from tru.models import Tru


class TruViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """Все наименования"""

    permission_classes = (IsAuthenticated,)
    serializer_class = TruSerializer

    def get_queryset(self):
        return Tru.objects.all()

    @action(
        methods=['get'], detail=False,
        url_path=r'(?P<sup_username>[^/.]+)/for-supplier'
    )
    def for_supplier(self, request, sup_username=None):
        a=1