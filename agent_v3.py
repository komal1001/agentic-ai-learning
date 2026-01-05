def agent(goal, text):
    goal_lower = goal.lower()

    if "summarize" in goal_lower:
        action = "summarize"
        reason = "Goal contains the word 'summarize'."
    elif "keyword" in goal_lower:
        action = "extract_keywords"
        reason = "Goal contains the word 'keyword' or 'keywords'."
    else:
        action = "do nothing"
        reason = "Goal does not match known actions."

    if action == "summarize":
        result = text[:50] + "..."
    elif action == "extract_keywords":
        words = text.split()
        result = ", ".join(words[:5])
    else:
        result = "No action taken."

    return action, reason, result


if __name__ == "__main__":
    text = "Agentic AI systems take goals, decide actions, and produce results."

    goals = [
        "Summarize this text",
        "Extract keywords from this text",
        "Translate this text"
    ]

    for goal in goals:
        action, reason, output = agent(goal, text)
        print("\nGOAL:", goal)
        print("DECISION:", action)
        print("WHY:", reason)
        print("RESULT:", output)
