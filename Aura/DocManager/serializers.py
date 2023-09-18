from rest_framework import serializers
from .models import *


class docmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = docma
        fields = '__all__'
