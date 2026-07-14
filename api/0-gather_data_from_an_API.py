#!/usr/bin/python3
"""Returns an employee's TODO list progress."""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
    )

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    employee_name = user_info["name"]

    completed_tasks = [task for task in todos_info if task["completed"]]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            len(completed_tasks),
            len(todos_info)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task["title"]))
