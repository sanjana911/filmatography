from django.db import models

# Create your models here.


class Actors(models.Model):

    name = models.CharField(max_length=200)

    age = models.PositiveIntegerField()

    gender_options =(
        ("female","female"),
        ("male","male")
    )

    gender = models.CharField(max_length=200, choices=gender_options)

    movie_name = models.CharField(max_length=200)

    release_year = models.IntegerField()

    rating = models.DecimalField(max_digits=3,decimal_places=1)