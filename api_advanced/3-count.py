#!/usr/bin/python3
"""
Contains a recursive function that parses hot titles and counts keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively tallies occurrences of specified words in hot titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            w_lower = word.lower()
            counts[w_lower] = counts.get(w_lower, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Ubuntu; Linux x86_64)"}
    params = {"after": after} if after else {}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        for child in children:
            title = child.get("data", {}).get("title", "").lower()
            words_in_title = title.split()
            for word in words_in_title:
                if word in counts:
                    counts[word] += 1

        next_after = data.get("after")
        if next_after:
            return count_words(subreddit, word_list, next_after, counts)

        sorted_counts = sorted(
            counts.items(), key=lambda item: (-item[1], item[0])
        )
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
    except Exception:
        return
