#!/usr/bin/python3
"""Queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit
"""
from requests import get
from sys import argv


hotlist = []
after = None


def count_all(hotlist, word_list):
    """
    Returns a list containing the titles of all
    hot articles for a given subreddit
    """

    count_dic = {word.lower(): 0 for word in word_list}
    for title in hotlist:
        words = title.split(' ')
        for word in words:
            if count_dic.get(word) is not None:
                count_dic[word] += 1

    for key in sorted(count_dic, key=count_dic.get, reverse=True):
        if count_dic.get(key):
            for thing in word_list:
                if key == thing.lower():
                    print("{}: {}".format(thing, count_dic[key]))


def count_words(subreddit, word_list):
    global hotlist
    global after
    """
    Returns a list containing the titles of all hot articles for a
    given subreddit
    """

    head = {'User-Agent': 'global smile'}
    if after:
        count = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after), headers=head).json().get('data')
    else:
        count = get('https://www.reddit.com/r/{}/hot.json'.format(
            subreddit), headers=head).json().get('data')
    hotlist += [dic.get('data').get('title').lower()
                for dic in count.get('children')]
    after = count.get('after')

    if after:
        return count_words(subreddit, word_list)
    return count_all(hotlist, word_list)


if __name__ == "__main__":
    count_words(argv[1], argv[2].split(' '))
