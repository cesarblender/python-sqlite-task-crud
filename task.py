class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
    
    def mark_completed(self):
        self.completed = True
    
    # Used to display the task
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} - {status}"
