from django.urls import path
from rest_framework import routers
from .views import ShowroomUserViewSet

router = routers.SimpleRouter()
router.register(r'showroom_user', ShowroomUserViewSet, basename="showroom_user")

urlpatterns = router.urls


