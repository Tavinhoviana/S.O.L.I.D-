class APIConnector:
    def connect(self, username: str, password: str):
        print(f"Connected to API as {username}")
        return True


class TaskManager:
    def create_task(self):
        print("Task created successfully")

    def update_task(self):
        print("Task updated successfully")

    def remove_task(self):
        print("Task removed successfully")


class NotificationService:
    def send_notification(self, message: str):
        print(f"Notification sent: {message}")


class ReportService:
    def generate_report(self):
        print("Report generated successfully")

    def send_report(self):
        print("Report sent successfully")


class TaskHandler:
    def __init__(self):
        self.api = APIConnector()
        self.tasks = TaskManager()
        self.notifications = NotificationService()
        self.reports = ReportService()

    def process_tasks(self, username: str, password: str):
        if self.api.connect(username, password):
            self.tasks.create_task()
            self.tasks.update_task()
            self.tasks.remove_task()
            self.notifications.send_notification("Tasks processed successfully")
            self.reports.generate_report()
            self.reports.send_report()
        else:
            self.notifications.send_notification("Error processing tasks")