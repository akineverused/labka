from django.db import models

# Create your models here.

class Students(models.Model):

    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.name
