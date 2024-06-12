import tkinter as tk
from tracker import Tracker

class TimeTrackerApp:
    def __init__(self):
        self.tracker = Tracker()
        self.tracker.load_data()

        self.root = tk.Tk()
        self.root.title("Time Tracker")

        self.name_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Input for task/skill name
        tk.Label(self.root, text="Task/Skill Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=10)

        # Buttons for starting and stopping tracking
        tk.Button(self.root, text="Start Tracking", command=self.start_tracking).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Stop Tracking", command=self.stop_tracking).grid(row=1, column=1, padx=10, pady=10)

        # Listbox to show currently active trackables
        self.active_listbox = tk.Listbox(self.root)
        self.active_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Button for showing summary
        tk.Button(self.root, text="Show Summary", command=self.show_summary).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Text widget to display the summary
        self.summary_text = tk.Text(self.root, height=10, width=50)
        self.summary_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for saving and loading data
        tk.Button(self.root, text="Save Data", command=self.save_data).grid(row=5, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Load Data", command=self.load_data).grid(row=5, column=1, padx=10, pady=10)

        # Update the active list initially
        self.update_active_list()

    def start_tracking(self):
        name = self.name_var.get()
        if name:
            message = self.tracker.start_tracking(name)
            self.update_active_list()
        else:
            message = "Please enter a name."
        self.show_info(message)

    def stop_tracking(self):
        selected = self.active_listbox.curselection()
        if selected:
            name = self.active_listbox.get(selected[0])
            message = self.tracker.stop_tracking(name)
            self.update_active_list()
        else:
            message = "Please select a task or skill to stop."
        self.show_info(message)

    def update_active_list(self):
        self.active_listbox.delete(0, tk.END)
        active_trackables = self.tracker.get_active_trackables()
        for name in active_trackables:
            self.active_listbox.insert(tk.END, name)

    def show_summary(self):
        summary = self.tracker.show_summary()
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)

    def save_data(self):
        message = self.tracker.save_data()
        self.show_info(message)

    def load_data(self):
        message = self.tracker.load_data()
        self.update_active_list()
        self.show_info(message)

    def show_info(self, message):
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, message)

    def run(self):
        self.root.mainloop()
