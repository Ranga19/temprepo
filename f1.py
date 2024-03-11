from django.db import models
from rest_framework import serializers, viewsets, routers
from django.urls import path, include


class Author(models.Model):


name = models.CharField(max_length=100) 
birth_date = models.DateField()


class Book(models.Model):


title = models.CharField(max_length=100)
author = models.ForeignKey(Author, on_delete=models.CASCADE)
publication_date = models.DateField()


class AuthorSerializer(serializers.ModelSerializer):
class Meta:


model = Author
fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
class Meta:


model = Book
fields = '__all__'


class AuthorViewSet(viewsets.ModelViewSet):


queryset = Author.objects.all()
serializer_class = AuthorSerializer


def get_queryset(self):


return Author.objects.filter(name__icontains=self.request.query_params.get('name', '')) 


class BookViewSet(viewsets.ModelViewSet): 


queryset = Book.objects.all() 
serializer_class = BookSerializer 


def get_queryset(self):


return Book.objects.filter(author_id=self.request.query_params.get('author_id')) 
