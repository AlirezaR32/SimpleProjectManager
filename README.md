# SimpleProjectManager 🗂️

A simple project and task management system written in Python. This program allows users to create new projects, define tasks, assign tasks to users, update task statuses, and save all data to a JSON file.

## Features ✨
- Create new projects
- Add tasks to projects
- Assign tasks to users
- Update task status
- Display project information
- Save data to `project.json`

## How to Run 🚀
```bash
python project_manager.py
```
##Class Structure 🧱
- task: Represents a task with title, description, due date, and status
- user: Represents a user with name, ID, and a list of assigned tasks
- project: Represents a project with name, list of users, and list of tasks
##Data Storage 💾
All project data is saved in a project.json file using JSON format.
##TODO ✅
- Add ability to delete tasks or projects
- Display full task list per user
- Add graphical interface using Tkinter or PyQt
