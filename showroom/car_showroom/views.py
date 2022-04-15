from rest_framework.permissions import AllowAny, IsAdminUser
from core.permissions import IsCustomerUser, IsSupplierUser, IsCarShowroomUser
from rest_framework.decorators import action
from core.views import CustomViewSet
from .models import (
    Car,
    CarShowroom,
    ShowroomSellCar,
    Customer,
    Transaction,
    Supplier,
    SupplierSellCar
)
from .serializers import (
    CarSerializer,
    CarShowroomSerializer,
    ShowroomSellCarSerializer,
    CustomerSerializer,
    TransactionSerializer,
    SupplierSerializer,
    SupplierSellCarSerializer
)
from .filters import (
    CarFilter,
    CarShowroomFilter,
    ShowroomSellCarFilter,
    CustomerFilter,
    TransactionFilter,
    SupplierFilter,
    SupplierSellCarFilter,
)


# Create your views here.
class CarViewSet(CustomViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def get(self, request):
        return super(CarViewSet, self).get(request)

    @action(detail=False, permission_classes=[IsAdminUser, IsCarShowroomUser, IsSupplierUser], methods=['post'])
    def post(self, request):
        return super(CarViewSet, self).post(request)

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser, IsCarShowroomUser, IsSupplierUser])
    def put(self, request, pk=None):
        return super(CarViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'], permission_classes=[IsAdminUser, IsCarShowroomUser, IsSupplierUser])
    def delete(self, request, pk):
        return super(CarViewSet, self).delete(request, pk)


class CarShowroomViewSet(CustomViewSet):
    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer
    filterset_class = CarShowroomFilter

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def get(self, request):
        return super(CarShowroomViewSet, self).get(request)

    @action(detail=False, permission_classes=[IsAdminUser, IsCarShowroomUser], methods=['post'])
    def post(self, request):
        return super(CarShowroomViewSet, self).post(request)

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser, IsCarShowroomUser])
    def put(self, request, pk=None):
        return super(CarShowroomViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'], permission_classes=[IsAdminUser, IsCarShowroomUser])
    def delete(self, request, pk):
        return super(CarShowroomViewSet, self).delete(request, pk)


class ShowroomSellCarViewSet(CustomViewSet):
    queryset = ShowroomSellCar.objects.all()
    serializer_class = ShowroomSellCarSerializer
    filterset_class = ShowroomSellCarFilter

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def get(self, request):
        return super(ShowroomSellCarViewSet, self).get(request)

    @action(detail=False, permission_classes=[IsAdminUser, IsCarShowroomUser], methods=['post'])
    def post(self, request):
        return super(ShowroomSellCarViewSet, self).post(request)

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser, IsCarShowroomUser])
    def put(self, request, pk=None):
        return super(ShowroomSellCarViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'], permission_classes=[IsAdminUser, IsCarShowroomUser])
    def delete(self, request, pk):
        return super(ShowroomSellCarViewSet, self).delete(request, pk)


class CustomerViewSet(CustomViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter

    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser, IsCustomerUser])
    def get(self, request):
        return super(CustomerViewSet, self).get(request)

    @action(detail=False, permission_classes=[IsAdminUser, IsCustomerUser], methods=['post'])
    def post(self, request):
        return super(CustomerViewSet, self).post(request)

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser, IsCustomerUser])
    def put(self, request, pk=None):
        return super(CustomerViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'], permission_classes=[IsAdminUser, IsCustomerUser])
    def delete(self, request, pk):
        return super(CustomerViewSet, self).delete(request, pk)


class TransactionViewSet(CustomViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilter

    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser, IsCustomerUser])
    def get(self, request):
        return super(TransactionViewSet, self).get(request)

    @action(detail=False, permission_classes=[IsAdminUser, IsCustomerUser], methods=['post'])
    def post(self, request):
        return super(TransactionViewSet, self).post(request)

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser, IsCustomerUser])
    def put(self, request, pk=None):
        return super(TransactionViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'], permission_classes=[IsAdminUser, IsCustomerUser])
    def delete(self, request, pk):
        return super(TransactionViewSet, self).delete(request, pk)


class SupplierSellCarViewSet(CustomViewSet):
    queryset = SupplierSellCar.objects.all()
    serializer_class = SupplierSellCarSerializer
    filterset_class = SupplierSellCarFilter

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def get(self, request):
        return super(SupplierSellCarViewSet, self).get(request)

    @action(detail=False, permission_classes=[IsAdminUser, IsSupplierUser], methods=['post'])
    def post(self, request):
        return super(SupplierSellCarViewSet, self).post(request)

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser, IsSupplierUser])
    def put(self, request, pk=None):
        return super(SupplierSellCarViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'], permission_classes=[IsAdminUser, IsSupplierUser])
    def delete(self, request, pk):
        return super(SupplierSellCarViewSet, self).delete(request, pk)


class SupplierViewSet(CustomViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filterset_class = SupplierFilter

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def get(self, request):
        return super(SupplierViewSet, self).get(request)

    @action(detail=False, permission_classes=[IsAdminUser, IsSupplierUser], methods=['post'])
    def post(self, request):
        return super(SupplierViewSet, self).post(request)

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser, IsSupplierUser])
    def put(self, request, pk=None):
        return super(SupplierViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'], permission_classes=[IsAdminUser, IsSupplierUser])
    def delete(self, request, pk):
        return super(SupplierViewSet, self).delete(request, pk)
