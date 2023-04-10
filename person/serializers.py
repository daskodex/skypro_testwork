from rest_framework import serializers
from .models import SimplePerson


class SimplePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimplePerson
        fields = '__all__'

