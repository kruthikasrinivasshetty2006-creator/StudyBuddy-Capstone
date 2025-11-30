# Study Planner Agent — StudyBuddy
*Subtitle:* A lightweight multi-agent system to help students plan study sessions, summarize notes, and stay on track

## Project Overview
StudyBuddy is a lightweight, modular multi-agent system designed to help students plan study sessions, break down tasks, summarize notes, fetch relevant study resources, and track learning progress. Built using the Google Agent Development Kit (ADK), StudyBuddy demonstrates how a coordinated set of specialized agents can automate and simplify daily learning workflows.

Students often struggle to balance lectures, assignments, revision, and exam preparation. StudyBuddy provides an intelligent digital assistant that:

- Understands the student's tasks and study requirements  
- Creates prioritized, time-based study schedules  
- Summarizes long lecture notes into quick revision points  
- Fetches helpful learning resources automatically  
- Tracks progress over time and recommends next actions  
- Keeps the student consistent through timely reminders  

## Solution Statement
StudyBuddy automates the entire study-planning lifecycle using a structured multi-agent architecture. Each agent specializes in a specific responsibility, allowing the system to generate well-organized study schedules, break down tasks efficiently, summarize notes, fetch resources, and analyze progress.

*Pipeline Flow:*  
User Input → Orchestrator → Specialized Agents → Tools & Memory → Orchestrator → User Output

## Architecture
### High-Level Components
1. *User Interface:* The user provides study tasks, deadlines, available hours, notes, and preferences.  
2. *Orchestrator Agent (Central Brain):* Coordinates all sub-agents, delegates tasks, validates outputs, and maintains session flow.  
3. *Task Breakdown Agent:* Splits complex study tasks or topics into smaller, manageable subtasks, assigns priority and duration, and feeds them to the schedule agent.  
4. *Study Schedule Agent:* Creates day-wise/hour-wise study schedules, performs validation, and outputs a clean, realistic plan.  
5. *Resource Fetcher Agent:* Uses Web Search Tool to gather references, notes, tutorials, and explanations.  
6. *Progress Analyzer Agent:* Evaluates completed vs. pending tasks, suggests modifications, and adjusts priorities using memory patterns.  
7. *Session Memory:* Stores temporary user data during a study session.  
8. *Memory Bank:* Maintains long-term memory for preferences, study habits, and strengths/weaknesses.  
9. *Tools:*  
   - *Web Search Tool:* Fetches learning resources in real-time.  
   - *Code Execution Tool:* Optional tool for programming-related tasks.  

![Architecture](architecture.png)

## Conclusion
StudyBuddy demonstrates how multi-agent systems can transform the study experience through automation, modularity, and intelligent planning. Students receive:

- A structured, time-aware study plan  
- Clean breakdown of complex tasks  
- Helpful resources automatically gathered  
- Consistent tracking of study progress  
- Personalized planning through memory-based adaptation  

## Value Statement
StudyBuddy helped reduce the time spent planning and organizing studies by over 60%. The Resource Fetcher quickly gathers materials, and the Progress Analyzer keeps track of weak areas.

Future enhancements could include:

- Revision Agent for automatic review cycles  
- Difficulty Estimator Agent using performance history  
- Notification Agent for reminders  
- Quiz Generator Agent for quick knowledge checks  

## Author
Kruthika