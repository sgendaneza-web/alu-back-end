#!usr/bin/python3
if __name__ == "__main__":
    import json
    import sys
    import urllib.request

    """
    format the employees id with the url
    https://jsonplaceholder.typicode.com/users/{employees_id}
    after getting it from the command line using the sys module
    """
    employee_id = sys.argv[1]
    url1 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url2 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/"
    # create a request objects at first using urllib.request.Request()
    req_object1 = urllib.request.Request(url1, method="GET")
    req_object2 = urllib.request.Request(url2, method="GET")
    # fetch the resources using the request objects and the function
    # urllib.request.urlopen
    with urllib.request.urlopen(req_object1) as response_object1:
        response1 = json.load(response_object1)
    with urllib.request.urlopen(req_object2) as response_object2:
        response2 = json.load(response_object2)
    # create an empty list to store completed tasks
    completed_tasks = []
    # iterate through all task to get task with boolean value true
    for task in response1:
        if task['completed'] is not True:
            continue
        completed_tasks.append(task)
    # get length for completed task and all task (complete and incomplete)
    no_of_comptasks = len(completed_tasks)
    totalno_of_task = len(response1)
    # get the employee name
    employee_name = response2["name"]
    # display the required format in the docs
    print(f"Employee {employee_name} is done with tasks({no_of_comptasks}/\
{totalno_of_task}):")
    for comp_tasks in completed_tasks:
        print(f"\t {comp_tasks['title']}")#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys


def main():
    """main function"""
    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    response = requests.get(todo_url)

    total_questions = 0
    completed = []
    for todo in response.json():

        if todo['userId'] == user_id:
            total_questions += 1

            if todo['completed']:
                completed.append(todo['title'])

    user_name = requests.get(user_url).json()['name']

    printer = ("Employee {} is done with tasks({}/{}):".format(user_name,
               len(completed), total_questions))
    print(printer)
    for q in completed:
        print("\t {}".format(q))


if __name__ == '__main__':
    main()
