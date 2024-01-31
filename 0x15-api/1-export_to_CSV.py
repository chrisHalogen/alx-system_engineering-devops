#!/usr/bin/python3
"""export data to csv"""
import csv
import sys
import requests

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    employee_username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": id}).json()

    with open("{}.csv".format(id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [id, employee_username, todo.get("completed"), todo.get("title")]
         ) for todo in todos]