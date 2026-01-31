from profile import Profile
from tracker import LearningTracker
from daily_log import DailyLog
from streak import CodingStreak


def main():
    print("\n✨ Welcome to varshiniv.dev — Personal System ✨\n")

    # Profile
    me = Profile(
        name="Varshini V",
        role="Aspiring Software Engineer",
        bio="Building myself through consistency, clarity, and code.",
        skills=["Python", "Git", "Problem Solving"]
    )
    me.display()

    # Learning Tracker
    tracker = LearningTracker()
    tracker.show_progress()

    # Daily Log
    log = DailyLog()
    log.show_logs()

    # Coding Streak
    streak = CodingStreak()
    streak.mark_today()
    print(f"🔥 Coding days logged: {streak.current_streak()}\n")


if __name__ == "__main__":
    main()
