class LearningTracker:
    def __init__(self):
        self.logs = []

    def add_log(self, topic, status):
        self.logs.append({"topic": topic, "status": status})

    def show_progress(self):
        for log in self.logs:
            print(f"{log['topic']} -> {log['status']}")


if __name__ == "__main__":
    tracker = LearningTracker()
    tracker.add_log("Git & GitHub", "Completed")
    tracker.add_log("Python Intermediate", "In Progress")
    tracker.show_progress()
