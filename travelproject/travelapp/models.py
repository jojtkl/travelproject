from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    disc = models.TextField()


class person(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    deta = models.TextField()

    def __str__(self):
        return self.name
