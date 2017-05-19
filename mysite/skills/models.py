from django.db import models


class Skills(models.Model):
    technologies = models.TextField()
    frameworks = models.TextField()
    data_bases = models.TextField()
    tools = models.TextField()
    operating_systems = models.TextField()
    name = 'Skills'

    def __str__(self):
        return self.name
