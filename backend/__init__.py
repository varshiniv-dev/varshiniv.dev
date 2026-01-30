class Profile:
    def __init__(self, name, role, skills, interests):
        self.name = name
        self.role = role
        self.skills = skills
        self.interests = interests

    def summary(self):
        return f"{self.name} | {self.role}"

    def show_skills(self):
        return ", ".join(self.skills)

    def show_interests(self):
        return ", ".join(self.interests)


if __name__ == "__main__":
    me = Profile(
        name="Varshini V",
        role="Aspiring Software Engineer",
        skills=["Python", "Git", "Problem Solving"],
        interests=["Tech", "Design", "Learning", "Growth"]
    )

    print(me.summary())
    print("Skills:", me.show_skills())
    print("Interests:", me.show_interests())
