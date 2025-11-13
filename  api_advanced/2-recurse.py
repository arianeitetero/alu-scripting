#!/usr/bin/python3
"""
2-recurse
Recursively returns a list of all hot article titles for a subreddit.
"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot article titles, None if invalid subreddit."""
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ubuntu:2-recurse:v1.0 (by /u/yourusername)'}
    params = {'after': after} if after else {}
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get('data', {})
        children = data.get('children', [])
        for child in children:
            hot_list.append(child.get('data', {}).get('title'))
        if data.get('after'):
            return recurse(subreddit, hot_list, data['after'])
        return hot_list
    except Exception:
        return None
