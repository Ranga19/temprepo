from django.db import models
from rest_framework import serializers, viewsets

class Author(models.Model):
    """
    a
    """
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

class Book(models.Model):  
    """b"""
    title = models.CharField(max_length=100) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
 
class AuthorSerializer(serializers.ModelSerializer):
    """c"""  
    class Meta:
        model = Author 
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    """c""" 
    class Meta: 
        model = Book
        fields = '__all__'

class AuthorViewSet(viewsets.ModelViewSet):
    """d"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return Author.objects.filter(name__icontains=self.request.query_params.get('name', ''))

class BookViewSet(viewsets.ModelViewSet):
    """e"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(author_id=self.request.query_params.get('author_id'))
    