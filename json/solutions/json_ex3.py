#!/usr/bin/env python3
'''
json_ex3.py

A sample task list can be retrieved from
  https://jsonplaceholder.typicode.com/todos.
Get the task list from the above API.
Save the data to two local files, one that contains completed tasks
  and another one that contains incomplete tasks.
The JSON data written to the files should be formatted
  as minimally as possible (no spaces, newlines, etc).
The program should display the number of tasks we have completed.
'''

import json
import requests


def separate_tasks(tasks):
    completed = []
    incomplete = []
    for task in tasks:
        if task["completed"]:
            completed.append(task)
        else:
            incomplete.append(task)

    return completed, incomplete


def write_data(file_name, data):
    with open(file_name, "w") as out:
        json.dump(data, out, separators=(',', ':'))


def main():
    url = "http://localhost:5000/todolist"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode())
        done, todo = separate_tasks(data["data"])
        write_data("tasks_done.json", done)
        write_data("tasks_todo.json", todo)
    else:
        print("response status:", response.status_code)

    finished = len(done)
    print(f"{finished} of {finished + len(todo)} tasks are done")


if __name__ == "__main__":
    main()
