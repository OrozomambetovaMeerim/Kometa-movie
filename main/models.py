from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils import timezone



class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=255)
    produser = models.CharField(max_length=255)
    year = models.IntegerField()
    img = models.ImageField(upload_to='main', null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    is_publicated = models.BooleanField(default=True)
    url = models.URLField(blank=True)
 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['name']


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'жанр'
    verbose_name_plural = 'жанры'
    ordering = ['name']



class Reviews(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    text = models.TextField()
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', 
        on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)

def __str__(self):
    return f"{self.name} - {self.movie}"

class Meta:
    verbose_name = 'Отзыв'
    verbose_name_plural = 'Отзывы'
    ordering = ['name']


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=60)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'
    ordering = ['name']


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Message(models.Model):
    author_name = models.CharField(max_length=80)
    email = CharField(max_length=60)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['message']

    def __str__(self):
            return self.message
