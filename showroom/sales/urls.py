from django.urls import path
from rest_framework import routers
from .views import (
    CarShowroomSaleViewSet,
    SupplierSaleViewSet
)

router = routers.SimpleRouter()
router.register(r'showroom_sale', CarShowroomSaleViewSet, basename="showroom_sale")
router.register(r'supplier_sale', SupplierSaleViewSet, basename="supplier_sale")


urlpatterns = router.urls


