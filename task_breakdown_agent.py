# Task Breakdown Agent: Splits complex tasks into smaller subtasks

def breakdown_task(task):
    print(f"Task Breakdown Agent: splitting task '{task}' into subtasks")
    return [f"{task} - part 1", f"{task} - part 2"]

if _name_ == "_main_":
    breakdown_task("Example Task")
