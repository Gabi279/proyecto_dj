
from rest_framework import serializers

from .models import Proyectos

        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = ('__all__')

""" class ProjectVSerializer(serializers.Serializer):
    id = serializers.IntegerField() """

