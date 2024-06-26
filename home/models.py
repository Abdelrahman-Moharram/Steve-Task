from django.db import models

def imagesave(instance, filename):
    extension = filename.split(".")[-1]
    return "books/%s/%s.%s"%("images", instance.name.replace(' ', '_'), extension)



class Author(models.Model):
    name            = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name            = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.TextField()
    publish_at      = models.DateField(auto_now=False, auto_now_add=False)
    poster          = models.ImageField(default="books/images/default.png",upload_to=imagesave, null=True)
    price           = models.DecimalField(max_digits=5, decimal_places=0, default=0)

    category        = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    author          = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name
