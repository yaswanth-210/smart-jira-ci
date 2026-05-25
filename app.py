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
            summary = fields.get("summary", "No Summary")

            # ✅ Get priority
            priority = calculate_priority(issue)

            # 🔥 CI/CD decision logic
            if priority == "High":
                action = "Trigger CI/CD"

                # ✅ Pass task details to GitHub
                trigger_github_action(summary, priority)

            elif priority == "Medium":
                action = "Conditional Run"
            else:
                action = "Skip"

            # ✅ Append task data
            tasks.append({
                "key": issue.get("key", "N/A"),
                "summary": summary,
                "priority": priority,
                "action": action
            })

        except Exception as e:
            print("Error processing issue:", e)

    return render_template("dashboard.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)