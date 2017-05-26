from django.db import models


class WelcomeText(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Academics(models.Model):
    school_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    logo_url = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.school_name


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
    github_login = models.TextField(null=True, blank=True)
    keybase_login = models.TextField(null=True, blank=True)
    url_3 = models.URLField(null=True, blank=True)
    text = models.TextField(max_length=250, null=True, blank=True)
    pdf_url = models.TextField(default='link from cloud or drive',
                               max_length=250, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Experience(models.Model):
    company_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    logo_url = models.CharField(max_length=250)
    position = models.CharField(max_length=50)
    responsibilities = models.TextField(max_length=500)

    def __str__(self):
        return self.company_name


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


class Skills(models.Model):
    technologies = models.TextField()
    frameworks = models.TextField()
    data_bases = models.TextField()
    tools = models.TextField()
    operating_systems = models.TextField()
    name = 'Skills'

    def __str__(self):
        return self.name
