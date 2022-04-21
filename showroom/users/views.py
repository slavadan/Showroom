from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from core.permissions import IsSupplierUser, IsCarShowroomUser
from rest_framework.decorators import action
from core.views import CustomViewSet
from .models import ShowroomUser
from .serializers import ShowroomUserSerializer


# Create your views here.
class ShowroomUserViewSet(CustomViewSet):
    queryset = ShowroomUser.objects.all()
    serializer_class = ShowroomUserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('username', )

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def get(self, request):
        return super(ShowroomUserViewSet, self).get(request)

    @action(detail=False, permission_classes=[IsAdminUser], methods=['post'])
    def post(self, request):
        return super(ShowroomUserViewSet, self).post(request)

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser])
    def put(self, request, pk=None):
        return super(ShowroomUserViewSet, self).put(request, pk)

    @action(detail=True, methods=['delete'], permission_classes=[IsAdminUser])
    def delete(self, request, pk):
        return super(ShowroomUserViewSet, self).delete(request, pk)

