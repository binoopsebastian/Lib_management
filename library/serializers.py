from rest_framework import serializers
from .models import Author, Book, Borrower


# Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']


# Book Serializer (shows author details)
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_id', 'published_date', 'available_copies']


# Borrower Serializer
class BorrowerSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Borrower
        fields = ['id', 'name', 'email', 'book', 'book_id', 'borrowed_date', 'return_date']
    
    def validate_book_id(self, value):
        """Check if book has available copies"""
        try:
            book = Book.objects.get(id=value)
            if book.available_copies <= 0:
                raise serializers.ValidationError("No copies available for this book.")
            return value
        except Book.DoesNotExist:
            raise serializers.ValidationError("Book does not exist.")
    
    def create(self, validated_data):
        """Reduce available_copies when borrowing"""
        book_id = validated_data.get('book_id')
        book = Book.objects.get(id=book_id)
        book.available_copies -= 1
        book.save()
        return super().create(validated_data)