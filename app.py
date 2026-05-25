from flask import Flask, render_template
from jira_api import get_jira_tasks
from priority import calculate_priority
from ci_trigger import trigger_github_action

app = Flask(__name__)

@app.route('/')
def dashboard():
    data = get_jira_tasks()
    issues = data.get("issues", [])

    tasks = []

    for issue in issues:
        try:
            fields = issue.get("fields", {})

            priority = calculate_priority(issue)

            # 🔥 CI/CD decision logic
            if priority == "High":
                action = "Trigger CI/CD"
                trigger_github_action()   # 🚀 REAL TRIGGER
            elif priority == "Medium":
                action = "Conditional Run"
            else:
                action = "Skip"

            tasks.append({
                "key": issue.get("key", "N/A"),
                "summary": fields.get("summary", "No Summary"),
                "priority": priority,
                "action": action
            })

        except Exception as e:
            print("Error:", e)

    return render_template("dashboard.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)