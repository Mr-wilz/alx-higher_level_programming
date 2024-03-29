#!/usr/bin/python3
"""lists 10 recent commmits from a Github repo"""


import requests
import sys

def list_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repo_name, owner_name)
