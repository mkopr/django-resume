import dateutil.parser
import requests

DEFAULT_GITHUB_CLIENT_ID = '23700733'
DEFAULT_GITHUB_CLIENT_SECRET = '23700733'


def request_github_user(github_login,
                        client_id=DEFAULT_GITHUB_CLIENT_ID,
                        client_secret=DEFAULT_GITHUB_CLIENT_SECRET):

    github_user_api_url = (
        'https://api.github.com/users/'
        '{github_login}?client_id={client_id}&client_secret={client_secret}'
    )
    github_user_repos_api_url = 'https://api.github.com/users/{}/repos'
    github_user_data = requests.get(github_user_api_url.format(
        github_login=github_login,
        client_id=client_id,
        client_secret=client_secret,
        )
    )

    github_user_repos_data = requests.get(
        github_user_repos_api_url.format(github_login),
    )

    github_user_data = github_user_data.json()
    github_user_repos_data = github_user_repos_data.json()

    return {
        'login': github_user_data['login'],
        'avatar_url': github_user_data['avatar_url'],
        'user_name': github_user_data['name'],
        'repos': github_user_repos_data,
        'account_created_at': (
            dateutil.parser.parse(github_user_data['created_at'])
        ),
        'account_url': github_user_data['html_url'],
    }