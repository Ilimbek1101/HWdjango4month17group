from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class Director(models.Model):
    class Meta:
        verbose_name = 'режиссер'
        verbose_name_plural = 'режиссеры'
    name = models.CharField(max_length=1000, unique=True, verbose_name='Имя режиссера')

    def __str__(self):
        return self.name


class Movie(models.Model):
    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                 null=True, verbose_name='Режиссер')
    title = models.CharField(max_length=1000, unique=True, verbose_name='Название фильма')
    description = models.TextField(blank=True, verbose_name='Описание фильма')
    image = models.ImageField(upload_to='movies', null=True, verbose_name='Картинка')

    def __str__(self):
        return self.title

    def image_img(self):
        if self.image:
            return mark_safe(f'<img src={self.image.url} width=300px')
        return mark_safe(f'<img src="https://sun9-78.userapi.com/impf/WR3VxYx35R4UBV671xOXrFoa2OHcjTIjxligrA/N19XS6EMXbc.jpg?size=1590x400&quality=95&crop=0,0,1590,400&sign=de1814451347fab3d0115c2d06e1d0dc&type=cover_group" style="width: 300px">')




class Review(models.Model):
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              null=True, verbose_name='Фильм')
    text = models.TextField(verbose_name='Текст отзыва')

    def __str__(self):
        return self.text
