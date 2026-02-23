# models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    release_date = models.DateField()
    showtimes = models.CharField(max_length=100, default="09:00,12:00,15:00,18:00,21:00")

    def __str__(self):
        return self.title

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=1)
    row = models.IntegerField()
    column = models.IntegerField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f'Seat {self.row}-{self.column}'