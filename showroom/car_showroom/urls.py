from django.urls import path
from rest_framework import routers
from .views import (
    CarViewSet,
    CarShowroomViewSet,
    ShowroomSellCarViewSet,
    CustomerViewSet,
    TransactionViewSet,
    SupplierSellCarViewSet,
    SupplierViewSet
)

router = routers.SimpleRouter()
router.register(r'cars', CarViewSet, basename="cars")
router.register(r'showroom', CarShowroomViewSet, basename="showroom")
router.register(r'showroom_cars', ShowroomSellCarViewSet, basename="showroom_cars")
router.register(r'customer', CustomerViewSet, basename="customer")
router.register(r'transaction', TransactionViewSet, basename="transaction")
router.register(r'suppliers', SupplierViewSet, basename="suppliers")
router.register(r'supplier_cars', SupplierSellCarViewSet, basename="supplier_cars")


urlpatterns = router.urls


