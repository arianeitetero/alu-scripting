#!/usr/bin/python3
"""
Module: 1-top_ten
Queries Reddit API and prints the titles of the first 10 hot posts
for a given subreddit. Prints 'OK' if subreddit is invalid or request fails.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): Subreddit name

    Prints:
        Titles of posts or 'OK' if subreddit is invalid or fails.
    """
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "python:topten:v1.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if RESPONSE.status_code != 200:
            print("OK")
            return

        HOT_POSTS = RESPONSE.json().get("data", {}).get("children", [])
        if not HOT_POSTS:
            print("OK")
            return

        for post in HOT_POSTS[:10]:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("OK")
