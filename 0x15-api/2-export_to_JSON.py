#!/usr/bin/python3
""" export data to json """
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    employee_username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": id}).json()

    with open("{}.json".format(id), "w") as jsonfile:
        json.dump({id: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee_username
            } for todo in todos]}, jsonfile)
