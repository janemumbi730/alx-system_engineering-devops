#!/usr/bin/python3

"""Get 10 hot posts for a subreddit"""

import requests


def top_ten(subreddit):
    """Query number of subscribers in subreddit"""

    # url link to the reddit api
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # prevents 429 status code (Rate limit)
    headers = {"User-Agent": "Custom"}

    # retrieve only 10 results
    params = {"limit": 10}

    # send a GET request
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        # get http response and convert from json type
        data = response.json()

        hotposts = data['data']['children']

        # count = 0

        for child in hotposts:
            print(child['data']['title'])
            # if count < 10:
            #     print(child['data']['title'])
            #     count += 1
            # else:
            #     break

    else:
        print("None")
