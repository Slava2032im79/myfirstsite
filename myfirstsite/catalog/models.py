from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    complexity = models.DecimalField(max_digits=10, decimal_places=2)
    options = models.IntegerField(default=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.task}, {self.user}'



class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

image = models.ImageField(upload_to='https://klike.net/uploads/posts/2020-02/1581672873_29.jpg', blank=True)