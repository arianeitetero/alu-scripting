#!/usr/bin/python3
"""
3-count
Recursively counts keywords in all hot posts of a subreddit.
"""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """Count occurrences of keywords in hot post titles of a subreddit."""
    if counts is None:
        counts = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ubuntu:3-count:v1.0 (by /u/yourusername)'}
    params = {'after': after} if after else {}
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json().get('data', {})
        children = data.get('children', [])
        for child in children:
            title = child.get('data', {}).get('title', '').lower()
            for word in word_list:
                word_lower = word.lower()
                counts[word_lower] = counts.get(word_lower, 0) + title.split().count(word_lower)
        if data.get('after'):
            return count_words(subreddit, word_list, data['after'], counts)
        # Print sorted results
        for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
            if count > 0:
                print(f"{word}: {count}")
    except Exception:
        return
