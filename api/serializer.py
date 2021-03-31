from rest_framework import serializers
from .models import allans


class qusformserializer(serializers.Serializer):
    qno=serializers.IntegerField()
    qus=serializers.CharField(max_length=1000)
    op1=serializers.CharField(max_length=1000)
    op2 = serializers.CharField(max_length=1000)
    op3 = serializers.CharField(max_length=1000)
    op4 = serializers.CharField(max_length=1000)


class allansserializer(serializers.Serializer):
    qusno=serializers.IntegerField()
    qus=serializers.CharField(max_length=1000)
    ans=serializers.CharField(max_length=1000)

    def create(self,validate_data):
        return allans.objects.create(**validate_data)