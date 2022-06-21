from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                 null=True)
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              null=True)
    text = models.TextField()

    def __str__(self):
        return self.text
