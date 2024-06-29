from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

#read
@api_view(['GET'])
def Booklist(request):
    booksobj=BooksModel.objects.all() #queryset
    serializer=BookSerializer(booksobj,many=True)
    return Response(serializer.data)

#create
@api_view(['POST'])
def post_Book(request):
    booksobj=BooksModel.objects.all() #queryset
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update
@api_view(['POST'])
def update_Book(request,id):
    booksobj=BooksModel.objects.get(id=id) #queryset
    serializer=BookSerializer(instance=booksobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
