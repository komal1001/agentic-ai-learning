def agent(goal, text):
    if "summarize" in goal.lower():
        action = "summarize"
    elif "keyword" in goal.lower():
        action = "extract_keywords"
    else:
        action = "do nothing"

    if action == "summarize":
        result = text[:50] + "..."
    elif action == "extract_keywords":
        words = text.split()
        result = ", ".join(words[:5])
    else:
        result = "No action taken."

    return action, result


if __name__ == "__main__":
    goal = "Extract keywords from this text"
    text = "Agentic AI systems take goals, decide actions, and produce results."

    action, output = agent(goal, text)

    print("GOAL:", goal)
    print("DECISION:", action)
    print("RESULT:", output)
