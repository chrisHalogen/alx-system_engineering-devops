#!/usr/bin/python3

"""
1-top_ten.py : Top Ten
"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Parameters:
        subreddit (str): The name of the subreddit

    Returns:
        None
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {"User-agent": "Google Chrome Version 81.0.4044.129"}
    params = {"limit": 10}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    res = get(url, headers=user_agent, params=params)
    response = res.json()

    try:
        my_data = response.get("data").get("children")

        for i in my_data:
            print(i.get("data").get("title"))

    except Exception:
        print("None")
