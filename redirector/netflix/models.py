from django.db import models


class NetflixShow(models.Model):
    Title = models.CharField(max_length=250)
    ReleaseDate = models.DateTimeField(auto_now=False, null=False)
    Type = models.CharField(max_length=20)
    Rating = models.CharField(max_length=50)
    Quality = models.CharField(max_length=50)
    Starring = models.CharField(max_length=250)
    Category = models.CharField(max_length=50)
    Runtime = models.CharField(max_length=50)
    NetflixId = models.CharField(max_length=10)
    Language = models.CharField(max_length=50)
    Description = models.CharField(max_length=1000)
