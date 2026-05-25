def calculate_priority(issue):
    fields = issue.get("fields", {})
    summary = fields.get("summary", "")

    # 🔥 Convert to lowercase safely
    summary_lower = summary.lower()

    print("DEBUG SUMMARY:", summary_lower)  # helps you verify

    # ✅ Smart keyword detection
    if "critical" in summary_lower or "failure" in summary_lower:
        return "High"
    elif "bug" in summary_lower:
        return "Medium"
    elif "performance" in summary_lower:
        return "High"
    elif "feature" in summary_lower:
        return "Low"
    else:
        return "Low"