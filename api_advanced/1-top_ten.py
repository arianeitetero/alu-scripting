#!/usr/bin/python3
"""
Module: 1-top_ten
This module contains the function `top_ten` that queries the Reddit API
and prints the titles of the first 10 hot posts for a given subreddit.

If the subreddit is invalid or the request fails, the function prints None.

Requirements:
- Do not follow redirects (invalid subreddits return redirects).
- Use the Reddit JSON API endpoint: /r/<subreddit>/hot.json
- Only the first 10 hot posts are printed.
"""

import requests


def top_ten(subreddit):
    import requests
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:topten:v1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print("Status code:", response.status_code)  # DEBUG

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        print("Posts found:", len(posts))  # DEBUG
        if not posts:
            print(None)
            return

        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except Exception as e:
        print("Exception:", e)
        print(None)
    """
    Prints the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): Name of the subreddit

    Prints:
        Titles of posts or None if subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:topten:v1.0"}  # username not needed

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Invalid subreddit → redirect or status code != 200
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        # Print first 10 post titles
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
