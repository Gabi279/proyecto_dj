
from rest_framework import serializers, pagination

from .models import User

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

""" class UserVSerializer(serializers.Serializer):
    id = serializers.IntegerField() """

