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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:topten:v1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Invalid subreddit or redirect
        if response.status_code != 200:
            print("OK")
            return

        posts = response.json().get("data", {}).get("children")
        if not posts:
            print("OK")
            return

        # Print first 10 titles
        for post in posts[:10]:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except Exception:
        print("OK")
