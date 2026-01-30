import json

class LearningTracker:
    def __init__(self, filename="progress.json"):
        self.filename = filename
        self.logs = self.load_logs()

    def load_logs(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def add_log(self, topic, status):
        self.logs.append({"topic": topic, "status": status})
        self.save_logs()

    def save_logs(self):
        with open(self.filename, "w") as file:
            json.dump(self.logs, file, indent=4)

    def show_progress(self):
        print("\nLearning Progress:")
        for log in self.logs:
            print(f"- {log['topic']} → {log['status']}")


if __name__ == "__main__":
    tracker = LearningTracker()
    tracker.add_log("Git Conflict Resolution", "Completed")
    tracker.add_log("Python Modules & Files", "In Progress")

    tracker.show_progress()