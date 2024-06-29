from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def home(request):
    student_obj = Student.object.all()
    serializer = Stud(student_obj,many=True)


    return Response({'status':200, 'payload':serializer.data})

StudentSerializer