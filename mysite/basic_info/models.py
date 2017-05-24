from django.db import models


# Create table for basic info on website abut me
class BasicInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    # Try ImageField
    photo_url = models.CharField(max_length=250, null=True, blank=True)
    birth_date = models.DateField()
    city = models.CharField(max_length=20)
    email = models.EmailField()
    # f.ex. 0048 000 000 000
    phone_number = models.IntegerField()
    url_1 = models.URLField(null=True, blank=True)
    url_2 = models.URLField(null=True, blank=True)
    url_3 = models.URLField(null=True, blank=True)
    text = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.first_name
