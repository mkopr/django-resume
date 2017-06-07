from django.db import models


class KeybaseKey(models.Model):
    login = models.CharField(max_length=39)
    public_key = models.TextField()
