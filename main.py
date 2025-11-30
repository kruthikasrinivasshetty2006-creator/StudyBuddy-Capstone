# Main program to run StudyBuddy

from orchestrator_agent import orchestrate
from task_breakdown_agent import breakdown_task
from study_schedule_agent import create_schedule
from resource_fetcher_agent import fetch_resources
from progress_analyzer_agent import analyze_progress

def run_studybuddy():
    orchestrate()
    tasks = breakdown_task("Study AI Agents")
    create_schedule(tasks)
    resources = fetch_resources("AI Agents")
    analyze_progress([], tasks)

if _name_ == "_main_":
    run_studybuddy()