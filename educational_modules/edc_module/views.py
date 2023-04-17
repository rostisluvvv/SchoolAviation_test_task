from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import EdcModule
from .serializers import EdcModuleSerializer


class EdcModuleViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = EdcModule.objects.all()
    serializer_class = EdcModuleSerializer
