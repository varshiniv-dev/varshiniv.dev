import json
from datetime import date


class DailyLog:
    def __init__(self, filename="daily_log.json"):
        self.filename = filename
        self.logs = self.load_logs()

    def load_logs(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_logs(self):
        with open(self.filename, "w") as file:
            json.dump(self.logs, file, indent=4)

    def add_entry(self, mood, hours, note):
        entry = {
            "date": str(date.today()),
            "mood": mood,
            "hours_spent": hours,
            "note": note
        }
        self.logs.append(entry)
        self.save_logs()

    def show_logs(self):
        for log in self.logs:
            print(
                f"{log['date']} | Mood: {log['mood']} | Hours: {log['hours_spent']}"
            )
            print(f"  → {log['note']}\n")


if __name__ == "__main__":
    log = DailyLog()
    log.add_entry(
        mood="calm but tired",
        hours=2,
        note="Even though Git drained me, I didn’t quit."
    )
    log.show_logs()
