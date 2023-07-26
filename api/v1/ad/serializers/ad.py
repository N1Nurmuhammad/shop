from rest_framework import serializersfrom accounts.models import CountryModelfrom api.v1.ad.serializers import SubCategoriesModelSerializer, CategoriesModelSerializerfrom apps.ad.models import *from api.v1.account.serializers import CountrySerializerclass AdPictureSerializer(serializers.ModelSerializer):    class Meta:        model = AdPictureModel        fields = '__all__'class AdLocationModelSerializer(serializers.ModelSerializer):    class Meta:        model = AdLocationModel        fields = '__all__'class AdSerializer(serializers.ModelSerializer):    is_liked = serializers.SerializerMethodField("get_is_liked")    pictures = serializers.SerializerMethodField("get_ad_pictures")    ad_owner_phone_number = serializers.SerializerMethodField("get_ad_owner_phone_number")    subcategory = SubCategoriesModelSerializer()    class Meta:        model = AdModel        fields = ['id', 'price', 'state', 'color', 'quantity', 'model', 'comment', 'ram', 'memory',                  'seen', 'discount_price', "category", "subcategory", 'is_liked', "pictures", "created_at",                  "ad_owner_phone_number"]    def get_is_liked(self, obj):        user = self.context.get("user", False)        if user:            return FavAdModel.objects.filter(ad=obj, owner=user).exists()        return False    def get_ad_pictures(self, obj):        ad_pictures = AdPictureModel.objects.filter(ad=obj)        serializer = AdPictureSerializer(ad_pictures, many=True)        return serializer.data    def get_ad_owner_phone_number(self, obj):        return obj.owner.phone_numberclass SearchSerializer(serializers.Serializer):    word = serializers.CharField(max_length=255)    class Meta:        fields = "__all__"