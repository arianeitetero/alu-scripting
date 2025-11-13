#!/usr/bin/python3
"""
1-top_ten
Prints titles of the first 10 hot posts for a subreddit.
"""
import requests

def top_ten(subreddit):
    """Print first 10 hot post titles of a subreddit, None if invalid."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'ubuntu:1-top-ten:v1.0 (by /u/yourusername)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)
