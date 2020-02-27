from rest_framework import serializers
from sockit.models import Sock

# Serializers
class SockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sock
        fields = '__all__'