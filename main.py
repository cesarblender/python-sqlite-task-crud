from database import conn
from task_list import TaskList

if __name__ == "__main__":
    task_list = TaskList()
    task_list.start()

conn.close()