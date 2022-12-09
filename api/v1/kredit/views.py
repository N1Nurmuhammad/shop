from kredit.models import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


@swagger_auto_schema(method="get", tags=["credit"], request_body=CreditModelSerializer)
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_credits(request):
    if not request.user.is_superuser:
        return Response(status=status.HTTP_403_FORBIDDEN)

    credits = CreditModel.objects.order_by('-created_date').all()
    serializer = CreditModelSerializer(credits, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method="get", tags=["credit"])
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_my_credit(request):
    user = request.user
    try:
        credit = CreditModel.objects.filter(account=user)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # if not (request.user.is_superuser or credit.account == request.user):
    #     return Response(status=status.HTTP_403_FORBIDDEN)

    serializer = CreditModelSerializer(credit, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method="post", tags=["credit"], request_body=CreditModelSerializer)
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_credit_view(request):
    user = request.user
    credit = CreditModel(account=user)
    serializer = CreditModelSerializer(credit, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(data=serializer.data)


@swagger_auto_schema(method="put", tags=["credit"], request_body=CreditModelSerializer)
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_credit_view(request, pk):
    user = request.user
    try:
        credit = CreditModel.objects.filter(account=user, pk=pk).frist()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CreditModelSerializer(credit, data=request.data)
    return Response(data=serializer.data)


@swagger_auto_schema(method="delete", tags=["credit"], request_body=CreditModelSerializer)
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_credit_view(request, pk):
    user = request.user

    try:
        credit = CreditModel.objects.get(account=user, pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    credit.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

