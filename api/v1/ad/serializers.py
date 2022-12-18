from rest_framework import serializers

from accounts.models.country import CountryModel
from app.models import *
from api.v1.account.serializers import CountrySerializer

class AdPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdPicturModel
        exclude = ['ad']


class AdSerializer(serializers.ModelSerializer):
# class CreateAdSerializer(serializers.ModelSerializer):
    picture = AdPictureSerializer(many=True)
    country = CountrySerializer()

    class Meta:
        model = AdModel
        fields = ['price', 'picture','country','state', 'color', 'quantity', 'model', 'comment', 'ram', 'memory', 'seen', 'dicount_price']

    def create(self, validated_data):
        pictures = validated_data.pop('picture')
        country = validated_data.pop('country')
        ad = AdModel.objects.create(**validated_data)
        for picture in pictures:
            AdPicturModel.objects.create(ad=ad, **picture)
        CountryModel.objects.create(ad=ad, **country)
        return ad
    def update(self, instance, validated_data):
        pictures = validated_data.pop('picture')
        country = validated_data.pop('country')
        return super().update(instance, validated_data)


class FavSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavAdModel
        fields = '__all__'


class SearchSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=255)

    class Meta:
        fields = "__all__"