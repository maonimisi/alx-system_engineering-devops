#!/usr/bin/python3

import requests


def top_ten(subreddit):
    '''function that queries the Reddit API and prints the titles
       of the first 10 hot posts listed for a given subreddit
    '''

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'maonimisi'}

    if subreddit is None or type(subreddit) != str:
        print(None)
    req = requests.get(url, headers=user_agent, allow_redirects=False,
                       params={'limit': 10}).json()
    data = req.get('data')
    if data:
        children = data.get('children')
    if data is not None and children is not None:
        for post in children:
            postData = post.get('data')
            title = postData.get('title')
            print(title)
    else:
        print('None')
