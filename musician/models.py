from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    instrument_type = models.TextField()

    def __str__(self) :
        return f"Name---{self.first_name}-{self.last_name}"