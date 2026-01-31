from datetime import date


class CodingStreak:
    def __init__(self):
        self.days = set()

    def mark_today(self):
        self.days.add(str(date.today()))

    def current_streak(self):
        return len(self.days)


if __name__ == "__main__":
    streak = CodingStreak()
    streak.mark_today()
    print(f"🔥 Coding days logged: {streak.current_streak()}")
