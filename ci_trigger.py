import requests
import os
from dotenv import load_dotenv

load_dotenv()

def trigger_github_action(task_name, priority):
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPO")

    url = f"https://api.github.com/repos/{repo}/dispatches"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "event_type": "trigger-ci",
        "client_payload": {
            "task": task_name,
            "priority": priority
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 204:
        print(f"✅ Triggered CI for: {task_name} ({priority})")
    else:
        print("❌ Failed to trigger CI/CD:", response.text)