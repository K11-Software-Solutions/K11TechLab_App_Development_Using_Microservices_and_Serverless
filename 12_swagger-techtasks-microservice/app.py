# Copied and adapted from Lab2 swagger_example
import os
import json
from flask import Flask, jsonify, make_response, request, send_from_directory
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

PORT = 5000

myApp = Flask(__name__)

# Load tasks from technology_tasks.json
TASKS_FILE = os.path.join(os.path.dirname(__file__), 'technology_tasks.json')
with open(TASKS_FILE, encoding='utf-8') as f:
    tasks = json.load(f)

@myApp.route('/swaggerfile_8')
def send_swagger():
    return send_from_directory('.', "swagger_config.json")

@myApp.route('/')
def get_home():
    return jsonify({'home': "tasks"})

@myApp.route('/tasks')
def get_tasks():
    return jsonify({'tasks': tasks})

@myApp.route('/task', methods=['POST'])
def add_tasks():
    data = request.get_json() or request.form
    name = data.get('name')
    description = data.get('description')
    if not name or not description:
        return "Missing 'name' or 'description'", 400
    task = {"name": name, "description": description}
    tasks.append(task)
    # Save to file
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
    return "Task Successfully added to the list"

@myApp.route('/task/<name>')
def get_task(name):
    filtered_task = list(filter(lambda task: task.get('name') == name, tasks))
    if len(filtered_task) == 0:
        return "No such task found"
    else:
        return jsonify(filtered_task)

@myApp.route('/task/<name>', methods=['DELETE'])
def delete_task(name):
    global tasks
    original_len = len(tasks)
    tasks = [task for task in tasks if task.get('name') != name]
    if len(tasks) < original_len:
        # Save to file
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
        return "Task deleted"
    else:
        return "No such task found"

if __name__ == "__main__":
    myApp.run(host="0.0.0.0", port=PORT, debug=True)
