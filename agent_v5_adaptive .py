memory = []

def agent(goal):

     goal_lower = goal.lower()

     for past in memory:
         if past["goal"] == goal_lower:
             print("I have done this before. skipping repeated work")
             return past["plan"]

     if "study" in goal_lower:
         plan=[ "open notes",
               "reading one topic",
               "write summary"
            
        ]
     elif "learn python" in goal_lower:
          plan=["open editor",
          "write small problems",
          "run program"
        
    ]
     else:
         plan=["do nothing"]


     for step in plan:
         print("executing : ",step)

     memory.append({
         "goal" : goal_lower,
        "plan" : plan
    })

     return plan


if __name__ == "__main__":
    goals = ["study agentic ai", 
            "learn python", 
            "study agentic ai"
    ]

    for g in goals:
        print("\n----")
        print("GOAL : ",g)
        final_plan = agent(g)
        print("FINAL PLAN : ",final_plan)

print("\nMEMORY : ", memory)    