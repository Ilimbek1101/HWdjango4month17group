from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[0:40]
