#!/usr/bin/python3
import requests
"""Count keywords for given list in reddit API"""


def count_words(subreddit, word_list, after=None, count=None, results=None):
        """Count keywords for given list in API reddit"""
    if after is None:
        count = {}
        results = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}
    headers = {'User-Agent': 'bhalut'}
    response = requests.get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for topic in data['data']['children']:
            title = topic['data']['title'].lower()
            for word in word_list:
                word = word.lower()
                if f" {word} " in f" {title} ":
                    if word in count:
                        count[word] += title.count(f" {word} ")
                    else:
                        count[word] = title.count(f" {word} ")

        after = data['data']['after']
        if after is None:
            for word in word_list:
                word = word.lower()
                if word in count:
                    results[word] = count[word]
            sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_results:
                print(f"{word}: {count}")
        else:
            count_words(subreddit, word_list, after, count, results)

if __name__ == '__main__':
    subreddit = "programming"
    word_list = ["javascript", "python", "java", "c++", "ruby"]

    count_words(subreddit, word_list)
