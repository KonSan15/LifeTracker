from trackable import Trackable
import json

class Tracker:
    def __init__(self):
        self.trackables = {}

    def start_tracking(self, name):
        if name in self.trackables:
            self.trackables[name].start()
        else:
            trackable = Trackable(name)
            trackable.start()
            self.trackables[name] = trackable
        return f"Started tracking {name}"

    def stop_tracking(self, name):
        if name in self.trackables and self.trackables[name].is_active:
            self.trackables[name].stop()
            return f"Stopped tracking {name}"
        else:
            return f"{name} is not currently being tracked."

    def get_active_trackables(self):
        return {name: t for name, t in self.trackables.items() if t.is_active}

    def show_summary(self):
        summary = []
        for name, trackable in self.trackables.items():
            summary.append(f"{name}: {trackable.get_elapsed_time()}")
        return "\n".join(summary)

    def save_data(self):
        try:
            with open("data.json", "w") as f:
                json.dump({name: trackable.total_time for name, trackable in self.trackables.items()}, f)
            return "Data saved successfully."
        except Exception as e:
            return f"Error saving data: {e}"

    def load_data(self):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
            for name, total_time in data.items():
                trackable = Trackable(name)
                trackable.total_time = total_time
                self.trackables[name] = trackable
            return "Data loaded successfully."
        except Exception as e:
            return f"Error loading data: {e}"
