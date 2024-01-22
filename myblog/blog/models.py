# blog/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    date_published = models.DateField()
    time_published = models.TimeField()
    datetime_published = models.DateTimeField()
    image = models.ImageField(upload_to='post_images/')
    integer_field = models.IntegerField()
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)

class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateField()
    time_commented = models.TimeField()
    datetime_commented = models.DateTimeField()
