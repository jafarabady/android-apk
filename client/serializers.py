from rest_framework import serializers

from client.models import Name


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'