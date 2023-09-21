from .models import SendLocationModel
from rest_framework import serializers


class SendLocationSerializers(serializers.ModelSerializer):

    class Meta:
        model = SendLocationModel
        fields = '__all__'