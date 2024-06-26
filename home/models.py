from django.db import models

class Author(models.Model):
    name            = models.CharField(max_length=150)

class Category(models.Model):
    name            = models.CharField(max_length=150)


class Book(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.TextField()
    publish_at      = models.DateField(auto_now=False, auto_now_add=False)
