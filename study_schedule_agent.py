# Study Schedule Agent: Creates a study plan

def create_schedule(tasks):
    print("Study Schedule Agent: creating schedule...")
    for task in tasks:
        print(f"Scheduled: {task}")

if _name_ == "_main_":
    create_schedule(["Task 1", "Task 2"])
