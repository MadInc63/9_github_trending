import requests
from datetime import date, timedelta


def get_trending_repositories(top_size):
    one_week_ago_date = date.today() - timedelta(days=7)
    git_hub_url = 'https://api.github.com/search/repositories'
    search_params = {
        'q': 'created:>{}'.format(one_week_ago_date),
        'page': '1',
        'per_page': top_size,
        'sort': 'stars',
        'order': 'desc'
    }
    responce = requests.get(git_hub_url, search_params)
    repository_list = responce.json()['items']
    return repository_list


def get_open_issues_amount(repo_owner, repo_name):
    issues_url = "https://api.github.com/repos/{owner}/{repo}/issues".format(
                  owner=repo_owner, repo=repo_name)
    response = requests.get(issues_url)
    return len(response.json())


if __name__ == '__main__':
    top_size = 20
    trending_repositories = get_trending_repositories(top_size)
    for repo in trending_repositories:
        repo_open_issues = get_open_issues_amount(repo['owner']['login'],
                                                  repo['name'])
        print('--------------------------------------------------------------')
        print("Repository owner: {owner}\nRepository name: {name}"
              "\nURL: {repo_url}\nOpen issues: {issues}"
              .format(owner=repo['owner']['login'],
                      name=repo['name'],
                      repo_url='{owners_html_url}/{repo_name}'
                               .format(
                               owners_html_url=repo['owner']['html_url'],
                               repo_name=repo['name']),
                      issues=repo_open_issues))
