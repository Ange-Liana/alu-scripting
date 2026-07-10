#!/usr/bin/python3
"""
Contains a recursive function that fetches all hot article titles.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches all hot titles from a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Ubuntu; Linux x86_64)"}
    params = {"after": after} if after else {}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])

        for child in children:
            hot_list.append(child.get("data", {}).get("title"))

        next_after = data.get("after")
        if next_after:
            return recurse(subreddit, hot_list, next_after)
        return hot_list
    except Exception:
        return None
