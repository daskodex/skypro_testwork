from rest_framework import serializers
from .models import SimplePerson


class SimplePersonSerializer(serializers.ModelSerializer):
    """ Сериалайзер для работы в SimplePerson """
    class Meta:
        model = SimplePerson
        fields = '__all__'

