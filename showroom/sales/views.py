from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAdminUser
from core.permissions import IsSupplierUser, IsCarShowroomUser
from .filters import CarShowroomSaleFilter, SupplierSaleFilter
from rest_framework.decorators import action
from core.views import CustomViewSet
from .models import (
    CarShowroomSale,
    SupplierSale
)
from .serializers import (
    CarShowroomSaleSerializer,
    SupplierSaleSerializer
)


# Create your views here.
class CarShowroomSaleViewSet(CustomViewSet):
    queryset = CarShowroomSale.objects.all()
    serializer_class = CarShowroomSaleSerializer
    filterset_class = CarShowroomSaleFilter

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def get(self, request):
        return super(CarShowroomSaleViewSet, self).get(request)

    @action(detail=False, permission_classes=[IsAdminUser, IsCarShowroomUser], methods=['post'])
    def post(self, request):
        return super(CarShowroomSaleViewSet, self).post(request)

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser, IsCarShowroomUser])
    def put(self, request, pk=None):
        return super(CarShowroomSaleViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'], permission_classes=[IsAdminUser, IsCarShowroomUser])
    def delete(self, request, pk):
        return super(CarShowroomSaleViewSet, self).delete(request, pk)


class SupplierSaleViewSet(CustomViewSet):
    queryset = SupplierSale.objects.all()
    serializer_class = SupplierSaleSerializer
    filterset_class = SupplierSaleFilter

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def get(self, request):
        return super(SupplierSaleViewSet, self).get(request)

    @action(detail=False, permission_classes=[IsAdminUser, IsSupplierUser], methods=['post'])
    def post(self, request):
        return super(SupplierSaleViewSet, self).post(request)

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser, IsSupplierUser])
    def put(self, request, pk=None):
        return super(SupplierSaleViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'], permission_classes=[IsAdminUser, IsSupplierUser])
    def delete(self, request, pk):
        return super(SupplierSaleViewSet, self).delete(request, pk)
