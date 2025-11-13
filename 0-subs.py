#!/usr/bin/python3
"""
0-subs
Queries Reddit API and returns the number of subscribers for a subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """Return number of subscribers for a given subreddit. 0 if invalid."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'ubuntu:0-subs:v1.0 (by /u/yourusername)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except Exception:
        return 0
