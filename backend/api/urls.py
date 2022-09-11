from rest_framework import routers

from api.views.contracts import (
    ConsumersViewSet, ContractsSViewSet,
    SupplierViewSet,
)
from api.views.tru import TruViewSet

app_name = 'api'


router = routers.SimpleRouter()

router.register(r'tru', TruViewSet, basename='tru')
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'consumers', ConsumersViewSet, basename='consumers')
router.register(r'contracts', ContractsSViewSet, basename='contracts')

urlpatterns = router.urls
