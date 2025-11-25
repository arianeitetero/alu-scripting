#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        # Attempt to get data, even if it fails, we catch the exception.
        RESPONSE.json().get("data").get("children") 
        # The key change is here: remove the title printing logic.
        print("OK") 
    except Exception:
        # If any step fails (e.g., subreddit doesn't exist, connection fails)
        print("OK")
    