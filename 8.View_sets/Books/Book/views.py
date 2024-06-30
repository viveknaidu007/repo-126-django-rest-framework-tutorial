from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets


# Create your views here.
class Studentviewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Student.objects.all()
        serializer=StudentSerializer(queryset,many=True)

    def retriever(self,request,pk=None):
        id=pk
        if id is not None:
                    queryset=Student.objects.all()
                    serializer=StudentSerializer(queryset,many=True)
                    return Response(serializer.data)
        

    def update(self,request,pk):
         id=pk
         queryset=Student.objects.get(pk=id)
         serializer=StudentSerializer(queryset,data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response({"msg":"complete data updated"})
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request):
         id=pk
         queryset=Student.objects.get(pk=id)
         queryset.delete()
         return Response({"msg":"deleted"})
    

    def create(self,request):
         serializer=StudentSerializer(data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response({"msg":"complete data created"})
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




# Create your views here.
class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

# Create your views here.
class Studentrev(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers


class StudentUp(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers


class StudentUp(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers


class Studentdel(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers


class Studentlc(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers


class Studentru(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers


class Studentrd(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers


class Studentrud(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

