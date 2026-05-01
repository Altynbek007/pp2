import json
import os
from datetime import datetime

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"

default_settings = {
    "sound": True,
    "car_color": "red",
    "difficulty": "normal"
}

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return default_settings
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)

def save_score(name, score, distance, difficulty):
    data = load_leaderboard()

    data.append({
        "name": name,
        "score": score,
        "distance": distance,
        "difficulty": difficulty,
        "date": datetime.now().strftime("%Y-%m-%d")
    })

    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)