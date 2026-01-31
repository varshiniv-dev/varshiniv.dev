import json
from datetime import date


class CodingStreak:
    def __init__(self, filename="backend/streak.json"):
        self.filename = filename
        self.days = self.load_days()

    def load_days(self):
        try:
            with open(self.filename, "r") as file:
                return set(json.load(file))
        except FileNotFoundError:
            return set()

    def save_days(self):
        with open(self.filename, "w") as file:
            json.dump(list(self.days), file, indent=4)

    def mark_today(self):
        self.days.add(str(date.today()))
        self.save_days()

    def current_streak(self):
        return len(self.days)


if __name__ == "__main__":
    streak = CodingStreak()
    streak.mark_today()
    print(f"🔥 Coding days logged: {streak.current_streak()}")
