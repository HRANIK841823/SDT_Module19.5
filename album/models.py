from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"Name---{self.name}"