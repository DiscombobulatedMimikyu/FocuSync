import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import get_json as db




class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        
        container = ctk.CTkFrame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (home_screen, name_screen, dashboard_screen, instructions_screen, add_task_screen, delete_task_screen, edit_task_screen, tasks_screen, productivity_screen):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(home_screen)

    def show_frame(self, cont):
        frame = self.frames[cont]

        if hasattr(frame, "reset"):
            frame.reset()

        frame.tkraise()

class home_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        no_text = ctk.CTkLabel(self, text = "")
        no_text.pack(pady=80)
        home_text = ctk.CTkLabel(self, text = 'WELCOME TO FOCUSYNC', font=("Arial", 50, "bold"))
        home_text.pack(pady=20)
        start_button = ctk.CTkButton(self, text = 'START', width = 200, height = 50, corner_radius=10, font=("Arial", 25, "bold"), fg_color='dodgerblue', text_color='black', command = lambda: controller.show_frame(name_screen))
        start_button.pack(pady=20)

class name_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        name_text = ctk.CTkLabel(self, text = 'Please Enter Name Here', font=("Arial", 40, "bold"))
        input_frame = ctk.CTkFrame(self)
        entry_string = tk.StringVar()
        output_string = tk.StringVar()
        input_entry = ctk.CTkEntry(master=input_frame, textvariable=entry_string, width = 400, height = 50, font=("Arial", 30))
        welcome_text = ctk.CTkLabel(self,
                                    text = '' ,
                                    font=("Arial", 25, "bold"),
                                    textvariable = output_string)
        no_text = ctk.CTkLabel(self, text = "")

        
        def welcome():
            name = entry_string.get()
            db.get_name(name)
            output_string.set(f'Hi {name}!\nWelcome To FocuSync\nThis Tool Helps You Beat Cramming By Managing Your Tasks And Schedules\nWith LED + Buzzer Reminders')
            welcome_text.pack(pady=40)
            add_task_button.pack(pady = 10)
            instructions_button.pack(pady = 10)
            enter_button.pack_forget()
            name_text.pack_forget()
            input_entry.pack_forget()
            input_frame.pack_forget()
        add_task_button = ctk.CTkButton(self,
                                            text = 'Continue',
                                            fg_color='dodgerblue', text_color='black',
                                             width = 200, height = 50, corner_radius=10, font=("Arial", 25),
                                            command = lambda: controller.show_frame(dashboard_screen))
        instructions_button = ctk.CTkButton(self,
                                                text= 'How It Works',
                                                width = 200, height = 50, corner_radius=10, font=("Arial", 25),
                                                fg_color='dodgerblue', text_color='black',
                                                command = lambda: controller.show_frame(instructions_screen))
        enter_button = ctk.CTkButton(self, text = 'Enter', fg_color='dodgerblue', width = 300, height = 40, font=("Arial", 25), command=welcome)
        no_text.pack(pady=50)
        name_text.pack(pady=60)
        input_entry.pack()
        input_frame.pack()
        enter_button.pack(pady=20)


        
class instructions_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        instructions_text = ctk.CTkLabel(self,
                                         text = f'HOW FOCUSYNC WORKS\nAdd Your Tasks and Schedule Time\nWhen A Task Starts, LED And Buzzer On The Device Will Activate\nPress STOP To Stop The Buzz\nWhen The Task Ends, It Will Be Logged In The Productivity Chart', font=("Arial", 25, "bold"))
        continue_button = ctk.CTkButton(self,
                                        text = 'Got It',
                                        fg_color='dodgerblue', font=("Arial", 25),
                                        text_color='black', width=200, height=50,
                                        command=lambda: controller.show_frame(dashboard_screen))
        no_text = ctk.CTkLabel(self, text = "")
        no_text.pack(pady=50)
        instructions_text.pack(pady=60)
        continue_button.pack()

tasks = db.load_data()

class dashboard_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        clock = ctk.CTkLabel(self)
     
        def now():
            current_time = datetime.now()
            string_time = current_time.strftime('%d/%m/%Y %I:%M %p')
            clock.configure(text=string_time)
            clock.after(1000, now)
        
        no_text = ctk.CTkLabel(self, text = "")        

        dashboard_label = ctk.CTkLabel(self,
                                       text = 'Dashboard', font=("Arial", 40, "bold"))
        
        add_task_button = ctk.CTkButton(self,
                                        text = 'Add',
                                        fg_color='dodgerblue', text_color='black',
                                        width = 300, height = 40, font=("Arial", 25),
                                        command = lambda: controller.show_frame(add_task_screen))
        delete_task_button = ctk.CTkButton(self,
                                        text = 'Delete',
                                        fg_color='dodgerblue', text_color='black',
                                        width = 300, height = 40, font=("Arial", 25),
                                        command = lambda: controller.show_frame(delete_task_screen))
        edit_task_button = ctk.CTkButton(self,
                                        text = 'Edit',
                                        fg_color='dodgerblue', text_color='black',
                                        width = 300, height = 40, font=("Arial", 25),
                                        command=lambda: controller.show_frame(edit_task_screen))
        tasks_button = ctk.CTkButton(self,
                                        text = 'Tasks',
                                        fg_color='dodgerblue', text_color='black',
                                        width = 300, height = 40, font=("Arial", 25),
                                        command = lambda: controller.show_frame(tasks_screen))
        now()
        no_text.pack()
        dashboard_label.pack(pady=80)
        add_task_button.pack(pady=10)
        delete_task_button.pack(pady=10)
        edit_task_button.pack(pady=10)
        tasks_button.pack(pady=10)
        clock.pack(side = 'bottom', anchor = 'e')
    
    def reset(self):
        global tasks
        tasks = db.load_data()

class add_task_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.edit_index = None
        self.step = 0
        self.values = {}

        self.prompts = [
            "Enter Task",
            "Enter Time (HH:MM AM/PM)",
            "Enter Date (DD/MM/YYYY)"
        ]

        self.title_label = ctk.CTkLabel(self, text="NEW TASK", font=("Arial", 30, "bold"))
        self.title_label.pack(pady=20)

        self.prompt_label = ctk.CTkLabel(self, text=self.prompts[self.step])
        self.prompt_label.pack(pady=10)

        self.entry_var = tk.StringVar()
        self.entry = ctk.CTkEntry(self, textvariable=self.entry_var, width=300)
        self.entry.pack(pady=10)

        self.feedback = ctk.CTkLabel(self, text="")
        self.feedback.pack(pady=10)

        self.enter_button = ctk.CTkButton(
            self,
            text="Enter",
            fg_color="dodgerblue",
            text_color="black",
            command=self.next_step
        )
        self.enter_button.pack(pady=10)

        self.save_button = ctk.CTkButton(
            self,
            text="Save",
            fg_color="dodgerblue",
            text_color="black",
            command=self.save_task
        )

        self.cancel_button = ctk.CTkButton(
            self,
            text="Cancel",
            fg_color="dodgerblue",
            text_color="black",
            command=lambda: controller.show_frame(dashboard_screen)
        )
        self.cancel_button.pack(pady=5)

    def next_step(self):
        value = self.entry_var.get().strip()
        if not value:
            self.feedback.configure(text="Please enter a value\n")
            return

        if self.step == 0:
            self.values["task"] = value
            self.feedback.configure(text=f"Task: {value}\n\n")

        elif self.step == 1:
            try:
                datetime.strptime(value, "%I:%M %p")
                self.values["time"] = value
                self.feedback.configure(
                    text=f"Task: {self.values['task']}\nTime: {value}\n"
                )
            except ValueError:
                self.feedback.configure(text="Invalid time format. Use HH:MM AM/PM")
                return

        elif self.step == 2:
            try:
                datetime.strptime(value, "%d/%m/%Y")
                self.values["date"] = value
                self.feedback.configure(
                    text=(
                        f"Task: {self.values['task']}\n"
                        f"Time: {self.values['time']}\n"
                        f"Date: {value}"
                    )
                )
                self.entry.configure(state='disabled')
                self.enter_button.pack_forget()
                self.cancel_button.pack_forget()
                self.save_button.pack(pady=10)
                self.cancel_button.pack(pady=5)
            except ValueError:
                self.feedback.configure(text="Invalid date format. Use DD/MM/YYYY")
                return

        self.step += 1
        self.entry_var.set("")
        if self.step < len(self.prompts):
            self.prompt_label.configure(text=self.prompts[self.step])

    def save_task(self):
        data = db.load_data()
        tasks = data.get("tasks", [])

        if self.edit_index is not None:
            tasks[self.edit_index] = self.values.copy()
            self.edit_index = None
        else:
            tasks.append(self.values.copy())

        data["tasks"] = tasks
        db.save_data(tasks=data["tasks"], points=data.get("points", 0))

        self.reset()
        self.controller.show_frame(dashboard_screen)

    def reset(self):
        self.step = 0
        self.values.clear()
        self.edit_index = None
        self.entry_var.set("\n\n")
        self.prompt_label.configure(text=self.prompts[0])
        self.feedback.configure(text="")
        self.save_button.pack_forget()
        self.cancel_button.pack_forget()
        self.entry.configure(state='normal')
        self.enter_button.pack(pady=10)
        self.cancel_button.pack(pady=5)

    def load_for_edit(self, index):
        self.reset()
        self.edit_index = index
        tasks = db.load_data()
        task_data = tasks[index]

        self.values = task_data.copy()

        self.entry_var.set(task_data["date"])
        self.prompt_label.configure(text="Edit Date (DD/MM/YYYY)")

        self.feedback.configure(
            text=(
                f"Task: {task_data['task']}\n"
                f"Time: {task_data['time']}\n"
                f"Date: {task_data['date']}"
            )
        )

        self.enter_button.pack_forget()
        self.cancel_button.pack_forget()
        self.save_button.pack(pady=10)
        self.cancel_button.pack(pady=5)
        
    def save_task(self):
        data = db.load_data()  # data is a dict with "tasks" and "points"
        tasks = data.get("tasks", [])

        if self.edit_index is not None:
            tasks[self.edit_index] = self.values.copy()
            self.edit_index = None
        else:
            data["tasks"].append(self.values.copy())

        data["tasks"] = tasks  # put updated tasks list back
        db.save_data(tasks=data["tasks"], points=data.get("points", 0))

        self.reset()
        self.controller.show_frame(dashboard_screen)

class delete_task_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.check_vars = []

        self.title = ctk.CTkLabel(self, text="Delete Tasks", font=("Arial", 30, "bold"))
        self.title.pack(pady=20)

        self.list_frame = ctk.CTkFrame(self)
        self.list_frame.pack(pady=10, fill="both", expand=True)

        self.delete_button = ctk.CTkButton(self, text="Delete Selected", fg_color="red",
                                           command=self.delete_selected)
        self.delete_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Back", fg_color="dodgerblue",
                                         command=lambda: controller.show_frame(dashboard_screen))
        self.back_button.pack(pady=5)

        self.populate_tasks()

    def populate_tasks(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        self.check_vars = []

        data = db.load_data()
        tasks = data.get("tasks", [])

        if not tasks:
            ctk.CTkLabel(self.list_frame, text="No tasks added yet").pack(pady=20)
            return

        for i, task in enumerate(tasks):
            var = tk.BooleanVar(value=False)
            chk = ctk.CTkCheckBox(
                self.list_frame,
                text=f"{task['task']} | {task['time']} | {task['date']}",
                variable=var
            )
            chk.pack(anchor="w", pady=5)
            self.check_vars.append((var, i))

    def delete_selected(self):
        data = db.load_data()
        tasks = data.get("tasks", [])
        to_delete = [i for var, i in self.check_vars if var.get()]
        if not to_delete:
            return

        for i in reversed(to_delete):
            del tasks[i]

        data["tasks"] = tasks
        db.save_data(tasks=data["tasks"], points=data.get("points", 0))
        self.populate_tasks()

    def reset(self):
        self.populate_tasks()
        
class edit_task_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.title_label = ctk.CTkLabel(self, text="Edit Task", font=("Arial", 30, "bold"))
        self.title_label.pack(pady=20)

        self.list_frame = ctk.CTkFrame(self)
        self.list_frame.pack(fill="both", expand=True, pady=10)

        self.select_button = ctk.CTkButton(
            self,
            text="Edit Selected",
            fg_color="dodgerblue",
            command=self.edit_selected
        )
        self.select_button.pack(pady=5)

        self.back_button = ctk.CTkButton(
            self,
            text="Back",
            fg_color="gray",
            command=lambda: controller.show_frame(dashboard_screen)
        )
        self.back_button.pack(pady=5)

        self.radio_var = tk.IntVar(value=-1)
        self.populate_tasks()

    def populate_tasks(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        self.radio_var.set(-1)
        data = db.load_data()
        tasks = data.get("tasks", [])

        if not tasks:
            ctk.CTkLabel(self.list_frame, text="No tasks to edit").pack(pady=20)
            return

        for i, t in enumerate(tasks):
            rb = ctk.CTkRadioButton(
                self.list_frame,
                text=f"{t['task']} | {t['time']} | {t['date']}",
                variable=self.radio_var,
                value=i
            )
            rb.pack(anchor="w", pady=4)

    def edit_selected(self):
        index = self.radio_var.get()
        if index < 0:
            return

        data = db.load_data()
        tasks = data.get("tasks", [])

        # Delete the selected task and save
        del tasks[index]
        data["tasks"] = tasks
        db.save_data(tasks=data["tasks"], points=data.get("points", 0))

        self.controller.frames[add_task_screen].reset()
        self.controller.show_frame(add_task_screen)

    def reset(self):
        self.populate_tasks()

class tasks_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.check_vars = []

        

        
        self.title_label = ctk.CTkLabel(self, text="Tasks", font=("Arial", 30, "bold"))
        self.title_label.pack(pady=10)
        self.progress_bar = ctk.CTkProgressBar(self, width=200, height=15, corner_radius=5)
        self.progress_bar.set(0)
        self.progress_bar.pack()
        self.points_var = tk.StringVar(value="Total Points: 0")
        self.points_label = ctk.CTkLabel(self, textvariable=self.points_var, font=("Arial", 25, "bold"))
        self.points_label.pack(pady=5)

        self.list_frame = ctk.CTkFrame(self)
        self.list_frame.pack(fill="both", expand=True, pady=10)

        self.complete_button = ctk.CTkButton(
            self,
            text="Completed Task/s",
            fg_color="green",
            command=self.complete_selected_tasks
        )
        self.complete_button.pack(pady=5)

        self.back_button = ctk.CTkButton(
            self,
            text="Back",
            fg_color="gray",
            command=lambda: controller.show_frame(dashboard_screen)
        )
        self.back_button.pack(pady=5)

        self.reset()

    def reset(self):
        data = db.load_data()
        tasks = [t for t in data.get("tasks", []) if not t.get("completed", False)]
        data["tasks"] = tasks
        db.save_data(tasks=tasks, points=data.get("points", 0))

        self.total_points = data.get("points", 0)
        self.populate_tasks()
        self.points_var.set(f"Total Points: {self.total_points}")

    def populate_tasks(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        self.check_vars = []

        data = db.load_data()
        tasks = data.get("tasks", [])

        if not tasks:
            ctk.CTkLabel(self.list_frame, text="No tasks added yet").pack(pady=20)
            return

        for i, task in enumerate(tasks):
            var = tk.BooleanVar(value=False)
            chk = ctk.CTkCheckBox(
                self.list_frame,
                text=f"{task['task']} | {task['time']} | {task['date']}",
                variable=var
            )
            chk.pack(anchor="w", pady=5)
            self.check_vars.append((var, i))

    def complete_selected_tasks(self):
        data = db.load_data()
        tasks = data.get("tasks", [])
        points_earned = 0
        remaining_tasks = []

        for var, i in self.check_vars:
            task = tasks[i]
            if var.get() and not task.get("completed", False):
                task["completed"] = True
                points_earned += 10
            remaining_tasks.append(task)
        self.progress_bar.set(points_earned*0.01)
        data["tasks"] = [t for t in remaining_tasks if not t.get("completed", False)]
        data["points"] = data.get("points", 0) + points_earned
        db.save_data(tasks=data["tasks"], points=data["points"])

        self.total_points = data["points"]
        self.points_var.set(f"Total Points: {self.total_points}")
        self.populate_tasks()
        
class productivity_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
app = App('FocuSync', (1000, 600))
app.mainloop()