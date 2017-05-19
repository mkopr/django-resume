from django.db import models


class Academics(models.Model):
    school_name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    logo_url = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.end_date
