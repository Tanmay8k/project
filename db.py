import json
import os
from datetime import datetime

FILE_NAME = "quiz_data.json"

def _load_data():
    if not os.path.exists(FILE_NAME):
        return {"questions": [], "scores": []}
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"questions": [], "scores": []}

def _save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def init_db():
    if not os.path.exists(FILE_NAME):
        _save_data({"questions": [], "scores": []})

def get_questions():
    data = _load_data()
    return data.get("questions", [])

def add_question(question, options, answer):
    data = _load_data()
    data["questions"].append({
        "question": question,
        "options": options,
        "answer": answer
    })
    _save_data(data)

def save_score(name, score, total):
    data = _load_data()
    data["scores"].append({
        "player": name,
        "score": score,
        "total": total,
        "played_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    _save_data(data)

def get_scores():
    data = _load_data()
    scores_list = []
    for item in data.get("scores", []):
        scores_list.append({
            "player": item.get("player", ""),
            "score": item.get("score", 0),
            "total": item.get("total", 0),
            "played_at": item.get("played_at", "")
        })
    return scores_list
