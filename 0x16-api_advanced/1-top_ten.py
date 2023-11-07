#!/usr/bin/python3

"""Get 10 hot posts for a subreddit"""

import requests


def top_ten(subreddit):
    """Query number of subscribers in subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {"User-Agent": "Custom"}

    params = {"limit": 10}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
 
        data = response.json()

        hotposts = data['data']['children']


        for child in hotposts:
            print(child['data']['title'])

    else:
        print("None")
