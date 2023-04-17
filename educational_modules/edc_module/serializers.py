from rest_framework import serializers

from .models import EdcModule


class EdcModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EdcModule
        fields = ('id', 'name', 'description', 'order_number')

