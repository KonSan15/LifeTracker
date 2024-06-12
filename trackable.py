import time

class Trackable:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.total_time = 0
        self.is_active = False

    def start(self):
        if not self.is_active:
            self.start_time = time.time()
            self.is_active = True

    def stop(self):
        if self.is_active:
            self.end_time = time.time()
            self.total_time += self.end_time - self.start_time
            self.is_active = False

    def get_elapsed_time(self):
        if self.is_active:
            current_time = time.time()
            elapsed_time = self.total_time + (current_time - self.start_time)
        else:
            elapsed_time = self.total_time
        return elapsed_time

    def format_time(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def __str__(self):
        return f"{self.name}: {self.format_time(self.get_elapsed_time())}"
    
    def get_current_session_time(self):
        if self.is_active:
            return time.time() - self.start_time
        return 0
