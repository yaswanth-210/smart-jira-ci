import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()

def get_jira_tasks():
    jira_url = os.getenv("JIRA_URL")
    email = os.getenv("JIRA_EMAIL")
    api_token = os.getenv("JIRA_API_TOKEN")

    url = f"{jira_url}/rest/api/3/search/jql"

    auth = HTTPBasicAuth(email, api_token)

    headers = {
        "Accept": "application/json"
    }

    params = {
        "jql": "project = TMP ORDER BY created DESC",
        "fields": ["summary", "issuetype", "priority"]
    }

    response = requests.get(url, headers=headers, params=params, auth=auth)

    if response.status_code != 200:
        print("Jira API Error:", response.text)
        return {}

    return response.json()