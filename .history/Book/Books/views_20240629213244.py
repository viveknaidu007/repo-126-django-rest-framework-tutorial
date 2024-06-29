from django.shortcuts import render
from .models import *
from .serializers import *
from rest_frameowrk.generics import GenericAPIview
from rest_framework.mixins import ListModelMixin

class Studentlist(GenericAPIview,ListModelMixin):
    queryset=Student.object.all()
    serializer_class=StudentSerializer
    def get(self,request):
        return self.list(request)