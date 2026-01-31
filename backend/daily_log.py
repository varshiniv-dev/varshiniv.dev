import json
from datetime import date


class DailyLog:
    def __init__(self, filename="backend/daily_log.json"):
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

    def add_entry(self):
        print("\n📝 Daily Check-In")

        mood = input("How do you feel today? → ")
        hours = input("How many hours did you work towards your goals? → ")
        note = input("What pushed you to show up today? → ")

        entry = {
            "date": str(date.today()),
            "mood": mood,
            "hours_spent": hours,
            "note": note
        }

        self.logs.append(entry)
        self.save_logs()
        print("\n✅ Entry saved.\n")

    def show_logs(self):
        print("\n📖 Past Entries:\n")
        for log in self.logs:
            print(
                f"{log['date']} | Mood: {log['mood']} | Hours: {log['hours_spent']}"
            )
            print(f"  → {log['note']}\n")


if __name__ == "__main__":
    log = DailyLog()
    log.add_entry()
    log.show_logs()
