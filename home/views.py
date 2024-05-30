from django.shortcuts import render
from home.models import Workshop
from .api_file.serializer import WorkshopSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Workshop_view (APIView):

    def get (self , request):
        workshop = Workshop.objects.all ()
        serializer = WorkshopSerializer (workshop , many=True)
        return Response (serializer.data)
    
    def post (self , request):
        serializer =WorkshopSerializer(data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else :
            return Response (serializer.errors)
        
class Workshop_detail (APIView):
    
    def get (self , request , pk):
        try :
            workshop = Workshop.objects.get (pk = pk)
        except :
            return Response ({'Error : Workshop not found'} , status=status.HTTP_404_NOT_FOUND)
        serializer = WorkshopSerializer (workshop)
        return Response (serializer.data)

    def post (self , request , pk):
        workshop = Workshop.objects.get (pk = pk)
        serializer = WorkshopSerializer (workshop , data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else :
            return Response (serializer.errors) 

    def delete (self , request , pk):
        workshop = Workshop.objects.get (pk = pk)
        workshop.delete ()
        return Response (status=status.HTTP_204_NO_CONTENT) 
