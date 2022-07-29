from django.shortcuts import render
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SearchSerializer
from .models import Data
# Create your views here.


class SearchAPIView_keb(APIView):
    def get(self,request,keb_text):
        data_get = Data.objects.get(keb = keb_text)
        if not data_get:
            return Response(data="can not get data", status=status.HTTP_400_BAD_REQUEST)
        else:
            data_get_serializer = SearchSerializer(data_get)
            return Response(data=data_get_serializer.data,status=status.HTTP_200_OK)

class SearchAPIView_reb(APIView):
    def get(self,request,reb_text):
        data_get = Data.objects.filter(reb = reb_text)
        if not data_get:
            return Response(data="can not get data", status=status.HTTP_400_BAD_REQUEST)
        else:
            data_get_serializer = SearchSerializer(data_get[1])
            return Response(data=data_get_serializer.data,status=status.HTTP_200_OK)

        
