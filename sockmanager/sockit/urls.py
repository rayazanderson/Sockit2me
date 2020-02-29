from rest_framework import routers
from .api import SockViewSet

router = routers.DefaultRouter()
router.register('api/leads', SockViewSet, 'leads')

urlpatterns = router.urls