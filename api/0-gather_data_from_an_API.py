#!/usr/bin/python3


"""
Retrieve and display the todo list progress for a specific employee.

Args:
employee_id (int): The ID of the employee for whom to fetch progress.

Returns:
None
"""

import requests
import sys

if __name__ == "__main__":

    """
    Gets the employee ID

    Puts the links of APIs into variables

    Retrieves data from the API and parses the data

    Uses the data to generate a progress report for each employee
    """

    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command line argument
    employee_id = sys.argv[1]

    # Define the API endpoints for todos and users
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    # Send HTTP GET requests to retrieve data from the API
    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    # Parse the JSON responses into Python dictionaries
    todo_data = todo_response.json()
    user_data = user_response.json()

    if 'name' in user_data:
        name = user_data['name']

    # Filter completed and total tasks for the specified employee
    completed_tasks = [task for task in todo_data
                       if task['userId'] == int(employee_id) and
                       task['completed']]
    total_tasks = [task for task in todo_data
                   if task['userId'] == int(employee_id)]

    # Display the employee's todo list progress
    fin = len(completed_tasks)
    sum = len(total_tasks)
    print(f"Employee {name} is done with tasks({fin}/{sum}):")
    for task in completed_tasks:
        print("\t " + task['title'])
