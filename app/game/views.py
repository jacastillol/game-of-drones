from rest_framework import viewsets, mixins

from core.models import Player
from game import serializers


class PlayerViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset = Player.objects.all()
    serializer_class = serializers.PlayerSerializer

    def get_queryset(self):
        """Return objects as a list"""
        return self.queryset.all().order_by('-name')

    def perform_create(self, serializer):
        """Create a new object"""
        if serializer.is_valid():
            serializer.save()
