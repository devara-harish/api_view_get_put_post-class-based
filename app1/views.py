from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from app1.serializers import *
from app1.models import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
class productcrud(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PJD=productserializers(PQS,many=True)
        return Response(PJD.data)
    

    def post(self,request):
        PMSD=productserializers(data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            return Response({'message':'product is created'})
        else:
            return Response({'failed':'product creation is failed'})
        



    def put(self,request):

        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=productserializers(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'product updated'})
        else:
            return Response({'failed':'product is not updated'})
        





