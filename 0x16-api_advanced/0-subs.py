#!/usr/bin/python3
"""
How many subs?
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Parameters:
        subreddit (str): The name of the subreddit

    Returns:
        int: The number of subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {"User-agent": "Google Chrome Version 81.0.4044.129"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    result = get(url, headers=user_agent)
    response = result.json()

    try:
        return response.get("data").get("subscribers")

    except Exception:
        return 0
