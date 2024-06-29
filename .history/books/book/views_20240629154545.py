from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def Booklist(request):
    booksobj=BooksModel.objects.all()
    serializer=BookSerializer(booksobj,many=True)
    return Response(serializer.data)