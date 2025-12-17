import json
import os

user = ""
DATA_FILE = ""

def get_name(name):
    global user, DATA_FILE
    user = name
    DATA_FILE = f"data/{user}.json"

    # Ensure the data folder exists
    os.makedirs("data", exist_ok=True)

    # If file doesn't exist, create with initial structure
    if not os.path.exists(DATA_FILE):
        initial_data = {
            "tasks": [],
            "points": 0
        }
        with open(DATA_FILE, "w") as f:
            json.dump(initial_data, f, indent=4)

def save_data(tasks=None, points=None):
    if not DATA_FILE:
        return

    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    # Load existing data if file exists
    data = {"tasks": [], "points": 0}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    if tasks is not None:
        data["tasks"] = tasks
    if points is not None:
        data["points"] = points

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    if not DATA_FILE or not os.path.exists(DATA_FILE):
        return {"tasks": [], "points": 0}
    with open(DATA_FILE, "r") as f:
        return json.load(f)