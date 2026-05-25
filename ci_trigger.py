import requests
import os
from dotenv import load_dotenv

load_dotenv()

def trigger_github_action():
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPO")

    url = f"https://api.github.com/repos/{repo}/dispatches"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "event_type": "trigger-ci"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 204:
        print("✅ CI/CD Triggered Successfully")
    else:
        print("❌ Failed to trigger CI/CD")
        print(response.text)