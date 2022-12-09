from rest_framework import serializers
from kredit.models import *


class CreditModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditModel
        fields = '__all__'