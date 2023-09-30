#!/usr/bin/python3
"""
a Python script that takes 2 arguments
in order to solve this challenge
"""


if __name__ == "__main__":
    import sys
    import requests

    repo_name = sys.argv[1]
    owner = sys.argv[2]
    r_url = ("https://api.github.com/repos/{}/{}/commits"
             .format(owner, repo_name))
    r = requests.get(r_url)
    data = r.json()
    i = 0
    for commit in data:
        if i == 10:
            break
        print("{}: {}".format(commit['sha'],
                              commit['commit']['author']['name']))
        i += 1
