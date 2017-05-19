from django.db import models


class Experience(models.Model):
    company_name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    logo_url = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    responsibilities = models.TextField(max_length=250)

    def __str__(self):
        return self.company_name
