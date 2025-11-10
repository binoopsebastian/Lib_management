from django.db import models

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    available_copies = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title


# Borrower Model
class Borrower(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowers')
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.book.title}"

