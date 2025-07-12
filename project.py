import json
class task ():
    def __init__ (self, name, description, date, status):
        self.name = name
        self.description = description
        self.date = date
        self.status = status
    
    def to_dict(self):
        return {
            'title': self.name,
            'description': self.description,
            'due_date': self.date,
            'status': self.status
        }

class user ():
    def __init__ (self, name, id):
        self.name = name
        self.id = id
        self.task = []
    def addTaskToUser (self, task):
        self.task.append(task)


#project class
class project ():
    def __init__ (self, name):
        self.name = name
        self.userlist = []
        self.tasklist = []

    def add_task (self, task):
        self.tasklist.append(task)

    def add_user (self, user):
        self.userlist.append(user)

    def getUserNames(self):
        return [user.name for user in self.userlist]

    def to_dict(self):
        return {
            'tasks': [task.to_dict() for task in self.tasklist],
            'users': self.getUserNames()
        }

#creating users
Alireza = user('Alireza', '@32')
all_users = {Alireza.name: Alireza}


#save

def saveData():
    data_to_save = {}
    for projectName, project in all_projects.items():
        data_to_save[projectName] = project.to_dict()
    fileName = "project.json"
    with open(fileName, 'w', encoding='utf-8') as f:
            json.dump(data_to_save,f)
            print(f"Data saved to {fileName}")

all_projects = {}
all_users = {Alireza: user('Alireza', '@32')} 
#main program
print('--- Project Management System ---')

while 1:
    choice = input(f'1.Create New Project \n 2.Add Task to Project \n 3.Assign Task to User \n 4.Update Task Status \n 5.Show Project Info \n 6.Save and Exit \n Select an option:')
    if choice == '1':
        print('--- Create New Project ---')
        projectName = input("Enter the project name: ")
        new_project = project(projectName)
        all_projects[projectName] = new_project
        print(f'Project "{projectName}" created successfully!')
    

    elif choice == '2':
        print('--- Add Task to Project ---')
        projectName = input("Enter the project name: ")
        taskname = input("Enter task title:")
        taskDescription = input("Enter task description:")
        taskDate = input("Enter task due date (YYYY-MM-DD):")
        newTask = task(taskname, taskDescription, taskDate, 'todo')
        all_projects[projectName].add_task(newTask)
        print(f'Task "{taskname}" added successfully to project "{projectName}"')

    elif choice == '3':
        print('--- Assign Task to User ---')
        projectName = input("Enter the project name: ")
        username = input("Enter user name:")
        taskname = input("Enter task name to assign:")
        usero = all_users.get(username)
        usero.addTaskToUser(taskname)
        all_projects[projectName].add_user(username)
        

        print(f'Task "{taskname}" assigned to user "{username}" in project "{projectName}"')    
    elif choice == '4':
        print('--- Update Task status ---')
        projectName = input("Enter the project name: ")
        taskname = input("Enter task title: ")
        status = input("Enter new status (todo/in-progress/completed):")
        if status in ['todo', 'in-progress', 'completed']:
            
            project_obj = all_projects.get(projectName)
            for t in project_obj.tasklist:
                if t.name == taskname:
                    task_to_update = t
            print(f'Task "{taskname}" status updated to "{status}"')
        else:
            print("Error")
    elif choice == '5':
        print('--- Show Project Info ---')
        projectName = input("Enter the project name: ")
        print(f'1.Project Name: {all_projects[projectName].name}')
        print(f'2.Description: {all_projects[projectName].tasklist[0].description}')
        print(f'3.Due Date: {all_projects[projectName].tasklist[0].date}')
        print(f'4.status: {all_projects[projectName].tasklist[0].status}')
        print(f'5.assigned to: {all_projects[projectName].getUserNames()}')
    elif choice == '6':
        print("Saving data to file...")
        saveData()
        print("Goodbye!")
        break
    else:
        print('Invalid choice. Please try again.')



