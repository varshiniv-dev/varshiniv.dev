class Profile:
    def __init__(self, name, role, bio, skills):
        self.name = name
        self.role = role
        self.bio = bio
        self.skills = skills

    def display(self):
        print(f"\n{self.name}")
        print(f"{self.role}")
        print("-" * 30)
        print(self.bio)
        print("\nSkills:")
        for skill in self.skills:
            print(f"- {skill}")


if __name__ == "__main__":
    me = Profile(
        name="Varshini V",
        role="Aspiring Software Engineer",
        bio="I’m building myself step by step through code, consistency, and curiosity.",
        skills=["Python", "Git", "Problem Solving"]
    )

    me.display()