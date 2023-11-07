#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'Maonimisi'}

    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
