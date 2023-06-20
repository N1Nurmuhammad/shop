from drf_yasg.utils import swagger_auto_schemafrom rest_framework import statusfrom rest_framework.decorators import api_view, permission_classes, authentication_classesfrom rest_framework.permissions import IsAuthenticatedfrom rest_framework.response import Responsefrom django.shortcuts import get_object_or_404from apps.ad.models import FavAdModelfrom api.v1.ad.serializers import FavSerializer, FavAdCreateSerializer@swagger_auto_schema(method="get", tags=["fav-ads"])@api_view(['GET'])@permission_classes((IsAuthenticated,))def get_fav_ad_view(request):    fav_ad = FavAdModel.objects.filter(owner=request.user)    serializer = FavSerializer(fav_ad, many=True, context={"user": request.user})    return Response(serializer.data)@swagger_auto_schema(method="get", tags=["fav-ads"])@api_view(['GET'])@permission_classes((IsAuthenticated,))def get_fav_ad_retrieve_view(request, pk):    room = get_object_or_404(FavAdModel, pk=pk, owner=request.user)    serializer = FavSerializer(room)    return Response(serializer.data)@swagger_auto_schema(method="post", tags=["fav-ads"], request_body=FavAdCreateSerializer)@api_view(['POST'])@permission_classes((IsAuthenticated,))def create_fav_ad_view(request):    room = FavAdModel(owner=request.user)    serializer = FavAdCreateSerializer(room, data=request.data)    if serializer.is_valid():        serializer.save()        return Response(serializer.data, status=status.HTTP_201_CREATED)    return Response(status=status.HTTP_400_BAD_REQUEST)@permission_classes((IsAuthenticated,))@swagger_auto_schema(method="put", tags=["fav-ads"], request_body=FavSerializer)@api_view(['PUT'])def update_fav_ad_view(request, pk):    fav_ad = get_object_or_404(FavAdModel, pk=pk)    serializer = FavSerializer(fav_ad, data=request.data)    if serializer.is_valid():        serializer.save()        return Response(serializer.data, status=status.HTTP_201_CREATED)    return Response(status=status.HTTP_400_BAD_REQUEST)@permission_classes((IsAuthenticated,))@swagger_auto_schema(method="delete", tags=["fav-ads"])@api_view(['DELETE'])def delete_fav_ad_view(request, pk):    fav_ad = FavAdModel.objects.filter(owner=request.user, ad__id=pk).first()    if fav_ad:        fav_ad.delete()        return Response(status=status.HTTP_204_NO_CONTENT)    return Response(status=status.HTTP_404_NOT_FOUND)