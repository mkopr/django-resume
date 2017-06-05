from django.db import models


class GithubUser(models.Model):
    login = models.CharField(max_length=39)
    avatar_url = models.URLField()
    user_name = models.CharField(max_length=255)
    repo_count = models.PositiveSmallIntegerField()
    account_created_at = models.DateTimeField()
    account_url = models.URLField()


class GithubRepo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    html_url = models.URLField()
    clone_url = models.URLField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    language = models.CharField(max_length=50)
    user = models.ForeignKey(GithubUser, related_name='repos', null=False)
