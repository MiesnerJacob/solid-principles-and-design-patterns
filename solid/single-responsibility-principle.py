# Single Responsibility Principle (SRP)

# Defintion: A class should have only one reason to change, meaning it should have only one job or responsibility. This helps to ensure that each class is focused and easier to maintain.

# ##################
# Bad Implementation
# ##################

# This ToDoList class handles multiple responsibilities including:
# - Managing tasks
# - Handling user input
# - Displaying tasks

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_tasks(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)

    def input_task(self):
        task = input("Enter a task: ")
        self.add_tasks(task)
                      
    def remove_task(self):
        task = input("Enter the task to remove: ")
        self.delete_task(task)

# Setup
print("Bad Implementaton (Single Responsiblity Principle)")
todo_list = ToDoList()

# Adding tasks
todo_list.input_task()  # Example: Enter a task: Buy groceries
todo_list.input_task()  # Example: Enter a task: Clean the house

# Display tasks
todo_list.display_tasks()

# Remove tasks
todo_list.remove_task()  # Example: Enter the task to remove: Buy groceries

# Display tasks again
todo_list.display_tasks()
print('\n')


# ###################
# Good Implementation
# ###################

# Responsibilities are separated into unique classes:
# - TaskManager: Manages tasks
# - TaskPresenter: Handles displaying tasks
# - TaskInput: Handles user input

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_tasks(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

class TaskPresenter:
    @staticmethod
    def display_tasks(tasks):
        for task in tasks:
            print(task)

class TaskInput:
    @staticmethod
    def input_task():
        return input("Enter a task: ")

    @staticmethod
    def remove_task():
        return input("Enter the task to remove: ")

# Setup
print("Good Implementaton (Single Responsiblity Principle)")
task_manager = TaskManager()
task_presenter = TaskPresenter()
task_input = TaskInput()

# Adding tasks
task = task_input.input_task()  # Example: Enter a task: Buy groceries
task_manager.add_tasks(task)

task = task_input.input_task()  # Example: Enter a task: Clean the house
task_manager.add_tasks(task)

# Display tasks
task_presenter.display_tasks(task_manager.tasks)

# Remove task
task = task_input.remove_task()  # Example: Enter the task to remove: Buy groceries
task_manager.delete_task(task)

# Display tasks again
task_presenter.display_tasks(task_manager.tasks)