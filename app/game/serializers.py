from rest_framework import serializers

from core.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    """Serializer for player objects"""

    class Meta:
        model = Player
        fields = ('name', 'victories', 'defeats')
