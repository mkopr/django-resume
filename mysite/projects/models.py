from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=50)
    language = models.TextField()
    technologies = models.TextField()
    URL = models.CharField(max_length=50)
    logo_url = models.CharField(max_length=250)
    device = models.TextField()
    description = models.TextField()
    finish = models.BooleanField(default=False)
    start_date = models.DateField()

    def __str__(self):
        return self.name
