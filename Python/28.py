import csv
import os

class Task:
    def __init__(self, name, description="", priority=1):
        self.name = name
        self.description = description
        self.priority = priority
        self.completed = False
        
    def mark_c(self):
        self.completed = True
        
    def __str__(self):
        status = "✅" if self.completed else "⬜"
        return f"{status} {self.name} (Priority: {self.priority})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)

    def show_tasks(self):
        if not self.tasks:
            print("📭 No tasks available!")
        for idx, task in enumerate(self.tasks):
            print(f"{idx + 1}. {task}")

    def save_csv(self, filename):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Description", "Priority", "Completed"])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority, task.completed])    
        print("task(s) saved.")
    
    
    def load_csv(self, filename):
            if not os.path.exists(filename):
                print("❌ File does not exist!")
                return
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.tasks = []
                for row in reader:
                    task = Task(row["Name"], row["Description"], int(row["Priority"]))
                    task.completed = row["Completed"] == "True"
                    self.tasks.append(task)


todo = ToDoList()
filename = "tasks.csv"
todo.load_csv(filename)

while True:
    print("\n>>>>>>>>>>>>>>>>>>>>> ToDo List <<<<<<<<<<<<<<<<<<<<<")
    print("1. Add New Task")
    print("2. Remove Task")
    print("3. Show All Tasks")
    print("4. Complete Task")
    print("5. Save to CSV")
    print("6. Load from CSV")
    print("7. Exit")

    choice = input("Please select: ")

    if choice == "1":
        name = input("Name: ")
        desc = input("Description: ")
        prio = int(input("Priority (number): "))
        task = Task(name, desc, prio)
        todo.add_task(task)
        print("Added task.")

    elif choice == "2":
        todo.show_tasks()
        index = int(input("Task number to remove: ")) - 1
        todo.remove_task(index)
        print("Deleted.")

    elif choice == "3":
        todo.show_tasks()

    elif choice == "4":
        todo.show_tasks()
        index = int(input("Task number to mark as completed: ")) - 1
        if 0 <= index < len(todo.tasks):
            todo.tasks[index].mark_c()
            print("Task marked as completed!")

    elif choice == "5":
        filename = input("filename to save: ")
        todo.save_csv(filename)

    elif choice == "6":
        filename = input("filename to load: ")
        todo.load_csv(filename)
        todo.show_tasks()

    elif choice == "7":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again!")
