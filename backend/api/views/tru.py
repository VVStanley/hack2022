from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.serializers.tru import DataTruSerializer
from tru.models import Tru


class TruViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = DataTruSerializer

    def get_queryset(self):
        return Tru.objects.all()
