from models.trackable import Trackable

def handle_start_tracking(app):
    selected = app.history_listbox.curselection()
    if selected:
        name = app.history_listbox.get(selected[0]).split(' - ')[0]
    else:
        name = app.new_task_var.get()
    if name:
        message = app.tracker.start_tracking(name)
        app.update_active_list()
    else:
        message = "Please enter a name or select a task from the history."
    app.show_info(message)

def handle_stop_tracking(app):
    selected = app.active_listbox.curselection()
    if selected:
        item_text = app.active_listbox.get(selected[0])
        name = item_text.split(' - ')[0]  # Extract the name only
        message = app.tracker.stop_tracking(name)
        app.update_active_list()
        app.update_history_list()  # Refresh the tracked programs list
    else:
        message = "Please select a task or skill to stop."
    app.show_info(message)

def handle_add_task(app):
    name = app.new_task_var.get()
    if name:
        app.tracker.trackables[name] = app.tracker.trackables.get(name, Trackable(name))
        app.update_history_list()
        app.new_task_var.set("")
    else:
        app.show_info("Please enter a task name.")
