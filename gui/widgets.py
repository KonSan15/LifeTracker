import tkinter as tk

def create_widgets(root, new_task_var):
    # Frame for left-side history list
    left_frame = tk.Frame(root)
    left_frame.grid(row=0, column=0, rowspan=7, padx=10, pady=10, sticky="ns")

    # Label and Listbox for history
    tk.Label(left_frame, text="Tracked Programs:").pack(anchor='w')
    history_listbox = tk.Listbox(left_frame, width=30, height=20)
    history_listbox.pack(fill='y', expand=True)

    # Input for new task/skill name
    tk.Entry(left_frame, textvariable=new_task_var).pack(pady=5, fill='x', expand=True)

    # Button for adding new task/skill
    add_task_button = tk.Button(left_frame, text="Add Task")
    add_task_button.pack(pady=5, fill='x', expand=True)

    # Frame for main tracking UI
    main_frame = tk.Frame(root)
    main_frame.grid(row=0, column=1, rowspan=6, padx=10, pady=10, sticky="nsew")

    # Buttons for starting and stopping tracking
    start_button = tk.Button(main_frame, text="Start Tracking")
    start_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    stop_button = tk.Button(main_frame, text="Stop Tracking")
    stop_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Listbox to show currently active trackables
    active_listbox = tk.Listbox(main_frame, width=50)
    active_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Button for showing summary
    show_summary_button = tk.Button(main_frame, text="Show Summary")
    show_summary_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Text widget to display the summary
    summary_text = tk.Text(main_frame, height=10, width=50)
    summary_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Buttons for saving and loading data
    save_button = tk.Button(main_frame, text="Save Data")
    save_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    load_button = tk.Button(main_frame, text="Load Data")
    load_button.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    return {
        'start_button': start_button,
        'stop_button': stop_button,
        'active_listbox': active_listbox,
        'history_listbox': history_listbox,
        'add_task_button': add_task_button,
        'show_summary_button': show_summary_button,
        'summary_text': summary_text,
        'save_button': save_button,
        'load_button': load_button
    }
