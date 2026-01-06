memory = []
def agent(goal):
    # Planning step



    if "study" in goal.lower():
        plan = [
            "open notes",
            "read one topic",
            "write summary"
        ]
    elif "learn python" in goal.lower():
        plan = [
            "open editor",
            "write small program",
            "run program"
        ]
    else:
        plan = ["do nothing"]

    # Execution step
    for step in plan:
        print("Executing:", step)
    

    memory.append(plan)

    return plan

final_plan = agent("study agentic ai")
print("FINAL PLAN:", final_plan)
print("MEMORY:", memory)

