from database import conn
from task_list import TaskList

if __name__ == "__main__":
    # Instantiate the task list class
    task_list = TaskList()

    # Show the menu options
    task_list.start()

# Close the database connection
conn.close()