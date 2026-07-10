#!/usr/bin/python3
"""
Contains a function that prints titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyRedditAPIClient/1.0 (by /u/alu_student)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            posts = data.get("children", [])
            if not posts:
                print(None)
                return
            for post in posts:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        print(None)
