#!/usr/bin/python3
"""
Contains a function that prints titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data")
            if data:
                children = data.get("children")
                if children and len(children) > 0:
                    for post in children:
                        print(post.get("data", {}).get("title"))
                    return
        print(None)
    except Exception:
        print(None)
