import json
from datetime import datetime


HISTORY_FILE = "data/history.json"


def clear_history():
    with open("data/history.json", "w") as file:
        json.dump([], file)


def save_history(text):
    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    history.append({
        "text": text,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    history = history[-10:]

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def get_history():
    with open(HISTORY_FILE, "r") as file:
        return json.load(file)
