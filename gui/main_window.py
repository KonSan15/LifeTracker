import tkinter as tk
from gui.widgets import create_widgets
from gui.handlers import handle_start_tracking, handle_stop_tracking, handle_show_summary, handle_save_data, handle_load_data, handle_add_task
from tracker import Tracker

class TimeTrackerApp:
    def __init__(self):
        self.tracker = Tracker()
        self.tracker.load_data()

        self.root = tk.Tk()
        self.root.title("Time Tracker")

        self.new_task_var = tk.StringVar()
        self.active_listbox = None
        self.history_listbox = None
        self.summary_text = None

        self.create_widgets()
        self.update_active_list()
        self.update_history_list()
        self.update_elapsed_time()

    def create_widgets(self):
        widgets = create_widgets(self.root, self.new_task_var)
        self.active_listbox = widgets['active_listbox']
        self.history_listbox = widgets['history_listbox']
        self.summary_text = widgets['summary_text']

        widgets['start_button'].config(command=lambda: handle_start_tracking(self))
        widgets['stop_button'].config(command=lambda: handle_stop_tracking(self))
        widgets['show_summary_button'].config(command=lambda: handle_show_summary(self))
        widgets['save_button'].config(command=lambda: handle_save_data(self))
        widgets['load_button'].config(command=lambda: handle_load_data(self))
        widgets['add_task_button'].config(command=lambda: handle_add_task(self))

    def update_active_list(self):
        selected_indices = self.active_listbox.curselection()
        self.active_listbox.delete(0, tk.END)
        active_trackables = self.tracker.get_active_trackables()
        for name in active_trackables:
            current_session_time = self.tracker.trackables[name].get_current_session_time()
            elapsed_time = self.tracker.trackables[name].get_elapsed_time()
            display_text = f"{name} - Current: {self.format_time(current_session_time)}, Total: {self.format_time(elapsed_time)}"
            self.active_listbox.insert(tk.END, display_text)
        for index in selected_indices:
            self.active_listbox.selection_set(index)

    def update_history_list(self):
        self.history_listbox.delete(0, tk.END)
        for name in self.tracker.trackables:
            total_time = self.tracker.trackables[name].get_elapsed_time()
            display_text = f"{name} - Total: {self.format_time(total_time)}"
            self.history_listbox.insert(tk.END, display_text)

    def update_elapsed_time(self):
        self.update_active_list()
        self.root.after(1000, self.update_elapsed_time)

    def show_info(self, message):
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, message)

    def format_time(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def run(self):
        self.root.mainloop()
