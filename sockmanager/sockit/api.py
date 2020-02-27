from sockit.models import Sock
from rest_framework import viewsets, permissions
from .serializers import SockSerializer

# Viewset
class SockViewSet(viewsets.ModelViewSet):
    queryset = Sock.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SockSerializer