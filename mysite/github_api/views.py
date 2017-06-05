import dateutil.parser
from django.http import HttpResponse
from django.shortcuts import render

from .models import GithubUser, GithubRepo
from .utils import request_github_user


def get_github_data(request, github_login):
    try:
        user = GithubUser.objects.get(login=github_login)
    except GithubUser.DoesNotExist:
        user_data = request_github_user(github_login)
        user = GithubUser(
            login=user_data['login'],
            avatar_url=user_data['avatar_url'],
            user_name=user_data['user_name'],
            repo_count=len(user_data['repos']),
            account_created_at=user_data['account_created_at'],
            account_url=user_data['account_url'],
        )
        user.save()

        for repository_data in user_data['repos']:
            repo = GithubRepo(
                name=repository_data['name'],
                description=repository_data['description'],
                html_url=repository_data['html_url'],
                clone_url=repository_data['clone_url'],
                created_at=(
                    dateutil.parser.parse(repository_data['created_at'])
                ),
                updated_at=(
                    dateutil.parser.parse(repository_data['updated_at'])
                ),
                language=repository_data['language'],
                user=user,
            )
            repo.save()

    return HttpResponse(status=200)
