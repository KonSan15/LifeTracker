def handle_show_summary(app):
    summary = app.tracker.show_summary()
    app.show_info(summary)

def handle_save_data(app):
    message = app.tracker.save_data()
    app.show_info(message)

def handle_load_data(app):
    message = app.tracker.load_data()
    app.update_active_list()
    app.update_history_list()
    app.show_info(message)
