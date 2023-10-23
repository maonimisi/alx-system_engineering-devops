#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(user_id), verify=False).json()

    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed_tasks), len(todo)))

    for task in completed_tasks:
        print("\t {}".format(task))

"""
    task_completed = []
    for task in todo:
        if task.get('completed') is True:
            task_completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(task_completed), len(todo)))

    for task in task_completed:
        print("\t {}".format(task))
"""
