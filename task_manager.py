class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

tasks = [Task("Learn Git", "High"), Task("Build Portfolio", "Medium")]
for t in tasks:
    print(f"Task: {t.name} | Priority: {t.priority}")
# Update v1.1 - Refactoring code
# Update v1.2 - Refactoring code
