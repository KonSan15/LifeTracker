import time

class Task:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.start_time = None
        self.total_time = 0
        self.is_active = False

    def start(self):
        self.start_time = time.time()
        self.is_active = True

    def stop(self):
        if self.is_active:
            self.total_time += time.time() - self.start_time
            self.start_time = None
            self.is_active = False

    def __str__(self):
        return f"Task: {self.name}, Skill: {self.skill}, Total Time: {self.total_time:.2f} seconds"
