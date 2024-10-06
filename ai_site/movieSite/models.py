from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(11), MaxValueValidator(110)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    STATUS_CHOICES = (
        ('pro', 'pro'),
        ('simple', 'simple')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple', null=True, blank=True)


class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(default=0)
    director_image = models.ImageField(upload_to='director_image/')

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(default=0)
    actor_image = models.ImageField(upload_to='director_image/')

    def __str__(self):
        return self.actor_name


class Janre(models.Model):
    janre_name = models.CharField(max_length=50)

    def __str__(self):
        return self.janre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    year = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    janre = models.ManyToManyField(Janre)
    TYP_CHOICES = (
        (144, 144),
        (360, 360),
        (480, 480),
        (720, 720),
        (1080, 1080)
    )
    types = models.IntegerField(choices=TYP_CHOICES, default=144)
    movie_time = models.SmallIntegerField(default=0)
    description = models.TextField()
    movie_trailer = models.FileField(null=True, blank=True, upload_to='trailer_video/')
    movie_image = models.ImageField(upload_to='movie_image/')
    movie = models.FileField(upload_to='movie/')
    STATUS_MOVIE = (
        ('pro', 'pro'),
        ('simple', 'simple')
    )
    status_movie = models.CharField(max_length=10, choices=STATUS_MOVIE, default='simple')

    def __str__(self):
        return self.movie_name

    def get_average_rating(self):
        ratings = self.comment.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


class MovieLanguages(models.Model):
    language = models.CharField(max_length=50)
    video = models.FileField(upload_to='lang_movie/')
    movie = models.ForeignKey(Movie, related_name='language', on_delete=models.CASCADE)


class Moments(models.Model):
    movie = models.ForeignKey(Movie, related_name='moments', on_delete=models.CASCADE)
    movie_moments = models.ImageField(upload_to='moments/')

    def __str__(self):
        return f'{self.movie}-{self.movie_moments}'


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='comment', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,11)], null=True, blank=True)
    parent = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.movie}'


class Favorite(models.Model):
    user = models.OneToOneField(Profile, related_name='favorite', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user}'


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, related_name='favorits', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cart} - {self.movie}'


class History(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.movie}'
