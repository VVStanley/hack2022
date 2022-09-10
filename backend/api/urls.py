from rest_framework import routers

from api.views.contracts import (
    ConsumerSViewSet, ContractsSViewSet,
    SupplierViewSet,
)
from api.views.tru import TruViewSet

app_name = 'api'


router = routers.SimpleRouter()

router.register(r'tru', TruViewSet, basename='tru')
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'consumer', ConsumerSViewSet, basename='consumer')
router.register(r'contracts', ContractsSViewSet, basename='contracts')

urlpatterns = router.urls
