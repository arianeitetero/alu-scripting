#!/usr/bin/python3
"""
Module: 1-top_ten
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit. Prints 'OK' if the subreddit is invalid or request fails.
"""

import requests


def top_ten(subreddit):
    """Prints the first 10 hot post titles or 'OK' if invalid subreddit."""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "python:topten:v1.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if RESPONSE.status_code != 200:
            print("OK")
            return

        HOT_POSTS = RESPONSE.json().get("data", {}).get("children")
        if not HOT_POSTS:
            print("OK")
            return

        for post in HOT_POSTS[:10]:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except Exception:
        print("OK")
