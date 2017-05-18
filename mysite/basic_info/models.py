from django.db import models


# Create table for basic info on website abut me
class BasicInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    # Try ImageField
    photo = models.CharField(max_length=20)
    birth_date = models.DateField()
    city = models.CharField(max_length=20)
    email = models.EmailField()
    # f.ex. 0048 000 000 000
    phone_number = models.IntegerField()
    url_1 = models.URLField()
    url_2 = models.URLField()
    url_3 = models.URLField()
    text = models.TextField(max_length=250)
    add_date = models.DateField()


    def __str__(self):
        return self.first_name
