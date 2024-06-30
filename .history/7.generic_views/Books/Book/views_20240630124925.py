from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView

# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers


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

