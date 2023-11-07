#!/usr/bin/python3
"""
Reddit API returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """returns number of total subscribers"""
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (0)
    response = response.json()
    if 'data' in response:
        return (response.get('data').get('subscribers'))

    else:
        return (0)
