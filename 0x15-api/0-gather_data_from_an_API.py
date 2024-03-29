#!/usr/bin/python3
""" Returns info about employee's todo list """
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed_task = [todo.get("title") for todo in todos
                      if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(completed_task), len(todos)))
    [print("\t {}".format(task)) for task in completed_task]
