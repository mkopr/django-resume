from django.db import models


class WelcomeText(models.Model):
    text = models.TextField()
    add_date = models.DateField()

    def __str__(self):
        return self.add_date
