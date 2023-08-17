from database import cursor, conn
from task import Task

class TaskList:
    def __init__(self):
        self.get_tasks()
    
    def get_tasks(self):
        cursor.execute("SELECT * FROM tasks")
        self.tasks = cursor.fetchall()

    def add_task(self, description):
        # Instantiate the task class
        task = Task(description)

        cursor.execute(
            "INSERT INTO tasks (description, done) VALUES (?, ?)",
            # If the tasks was complete, the value is 1, else is 0
            (task.description, 1 if task.completed else 0)
        )

        # Save changes
        conn.commit()
    
    def show_tasks(self):
        # Get all tasks from DB
        self.get_tasks()
        
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task[1]} - {'Completed' if task[2] else 'Pending'}")
    
    def mark_completed(self, index):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            cursor.execute("UPDATE tasks SET done = ? WHERE id = ?", (1, task[0]))
            conn.commit()
            print("Task marked as completed.")
        else:
            print("Invalid index.")
    
    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task[0],))
            conn.commit()
            print("Task deleted.")
        else:
            print("Invalid index.")
    
    def start(self):
        while True:
            print("\n--- Task List ---")
            print("1. Add task")
            print("2. Show tasks")
            print("3. Mark task as completed")
            print("4. Delete task")
            print("5. Exit")
            
            option = input("Select an option: ")
            
            if option == "1":
                description = input("Enter task description: ")
                self.add_task(description)
            elif option == "2":
                self.show_tasks()
            elif option == "3":
                index = int(input("Enter the task number to mark as completed: "))
                self.mark_completed(index)
            elif option == "4":
                index = int(input("Enter the task number to delete: "))
                self.delete_task(index)
            elif option == "5":
                break
            else:
                print("Invalid option. Please select a valid option.")
