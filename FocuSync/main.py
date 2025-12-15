import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import datetime

tasks = []
times = []
dates = []
ctk.set_default_color_theme("dark-blue")
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

        for F in (home_screen, name_screen, dashboard_screen, instructions_screen, add_task_screen, add_time_screen, add_date_screen, save_state, summary_screen, productivity_screen):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(home_screen)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class home_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        home_text = ctk.CTkLabel(self, 100, 100, text = 'WELCOME TO FOCUSYNC' )
        home_text.pack()
        start_button = ctk.CTkButton(self, text = 'START', fg_color='Blue', text_color='Black', hover_color='Red', command = lambda: controller.show_frame(name_screen))
        start_button.pack()

class name_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        name_text = ctk.CTkLabel(self, text = 'Please Enter Name Here') 
        name_text.pack()
        input_frame = ctk.CTkFrame(self)
        entry_string = tk.StringVar()
        output_string = tk.StringVar()
        input_entry = ctk.CTkEntry(master=input_frame, textvariable=entry_string)
        welcome_text = ctk.CTkLabel(self,
                                    text = '' ,
                                    textvariable = output_string)
        
        def welcome():
            name = entry_string.get()
            output_string.set(f'Hi {name}!\nWelcome To FocuSync\nThis Tool Helps You Beat Cramming By Managing Your Tasks And Schedules With LED + Buzzer Reminders')
            add_task_button = ctk.CTkButton(self,
                                            text = 'Continue',
                                            fg_color='Blue',
                                            hover_color='Red',
                                            command = lambda: controller.show_frame(dashboard_screen))
            instructions_button = ctk.CTkButton(self,
                                                text= 'How It Works',
                                                fg_color='Blue',
                                                hover_color='Red',
                                                command = lambda: controller.show_frame(instructions_screen))
            welcome_text.pack()
            add_task_button.pack()
            instructions_button.pack()
        enter_button = ctk.CTkButton(self, text = 'Enter', fg_color='Blue', hover_color='Red', command=welcome)
        enter_button.pack()
        input_entry.pack()
        input_frame.pack()
        
class instructions_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        instructions_text = ctk.CTkLabel(self,
                                         text = f'HOW FOCUSYNC WORKS\nAdd Your Tasks and Schedule Time\nWhen A Task Starts, LED And Buzzer On The Device Will Activate\nPress STOP To Stop The Buzz\nWhen The Task Ends, It Will Be Logged In The Productivity Chart',)
        continue_button = ctk.CTkButton(self,
                                        text = 'Got It',
                                        fg_color='Blue',
                                        hover_color='Red',
                                        command=lambda: controller.show_frame(dashboard_screen))
        instructions_text.pack()
        continue_button.pack()

class dashboard_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        time = ctk.CTkLabel(self)
        def now():
            current_time = datetime.datetime.now()
            string_time = current_time.strftime('%d %B, %Y %I:%M:%S %p') 
            time.configure(text=string_time)
    # Schedule the function to run again after 1000ms (1 second)
            time.after(1000, now)
        dashboard_label = ctk.CTkLabel(self,
                                       text = 'Dashboard')
        add_task_button = ctk.CTkButton(self,
                                        text = 'Add',
                                        fg_color='Blue',
                                        hover_color='Red',
                                        command = lambda: controller.show_frame(add_task_screen))
        delete_task_button = ctk.CTkButton(self,
                                        text = 'Delete',
                                        fg_color='Blue',
                                        hover_color='Red',
                                        command = lambda: controller.show_frame(add_task_screen))
        edit_task_button = ctk.CTkButton(self,
                                        text = 'Edit',
                                        fg_color='Blue',
                                        hover_color='Red',
                                        command = lambda: controller.show_frame(add_task_screen))
        summary_button = ctk.CTkButton(self,
                                        text = 'Edit',
                                        fg_color='Blue',
                                        hover_color='Red',
                                        command = lambda: controller.show_frame(summary_screen))
        now()
        dashboard_label.pack_configure(side = 'left', anchor='n')
        add_task_button.pack()
        delete_task_button.pack()
        edit_task_button.pack()
        time.pack_configure(side = 'left', anchor='n')

class add_task_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        new_task_label = ctk.CTkLabel(self,
                                      text = 'NEW TASK')
        input_frame = ctk.CTkFrame(self)
        entry_string = tk.StringVar()
        output_string = tk.StringVar()
        input_entry = ctk.CTkEntry(master=input_frame, 
                                   textvariable=entry_string)
        new_task  = ctk.CTkLabel(self,
                                 text = '',
                                textvariable = output_string)
        def add_task():
            task = entry_string.get()
            output_string.set('{task}')
            tasks.append(task)
            next_button_1 = ctk.CTkButton(self,
                                    text = 'Next',
                                    fg_color='Blue',
                                    hover_color='Red',
                                    command=lambda: controller.show_frame(add_time_screen))
            next_button_1.pack()
        enter_button = ctk.CTkButton(self,
                                    text = 'Next',
                                    fg_color='Blue',
                                    hover_color='Red',
                                    command=add_task)
        cancel_button = ctk.CTkButton(self,
                                    text = 'Next',
                                    fg_color='Blue',
                                    hover_color='Red',
                                    command=lambda: controller.show_frame(dashboard_screen))
        enter_button.pack()
        cancel_button.pack()
        new_task_label.pack()
        input_entry.pack()
        input_frame.pack()
class add_time_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        new_time_label = ctk.CTkLabel(self,
                                      text = 'NEW TASK')
        input_frame = ctk.CTkFrame(self)
        entry_string = tk.StringVar()
        output_string = tk.StringVar()
        input_entry = ctk.CTkEntry(master=input_frame, 
                                   textvariable=entry_string)
        new_time = ctk.CTkLabel(self,
                                text = '',
                                textvariable = output_string)
        def add_time():
            time = entry_string.get()
            output_string.set('{time}')
            times.append(time)
            next_button_2 = ctk.CTkButton(self,
                                    text = 'Next',
                                    fg_color='Blue',
                                    hover_color='Red',
                                    command=lambda: controller.show_frame(add_date_screen))
            next_button_2.pack()
        enter_button = ctk.CTkButton(self,
                                    text = 'Next',
                                    fg_color='Blue',
                                    hover_color='Red',
                                    command=add_time)
        cancel_button = ctk.CTkButton(self,
                                    text = 'Next',
                                    fg_color='Blue',
                                    hover_color='Red',
                                    command=lambda: controller.show_frame(dashboard_screen))
        
        enter_button.pack()
        cancel_button.pack()
        new_time_label.pack()
        input_entry.pack()
        input_frame.pack()
class add_date_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        new_date_label = ctk.CTkLabel(self,
                                      text = 'NEW TASK')
        input_frame = ctk.CTkFrame(self)
        entry_string = tk.StringVar()
        output_string = tk.StringVar()
        input_entry = ctk.CTkEntry(master=input_frame, 
                                   textvariable=entry_string)
        new_date = ctk.CTkLabel(self,
                                text = '',
                                textvariable = output_string)
        def add_date():
            date = entry_string.get()
            output_string.set('{date}')
            dates.append(date)
            next_button_3 = ctk.CTkButton(self,
                                    text = 'Next',
                                    fg_color='Blue',
                                    hover_color='Red',
                                    command=lambda: controller.show_frame(save_state))
            next_button_3.pack()
        enter_button = ctk.CTkButton(self,
                                    text = 'Next',
                                    fg_color='Blue',
                                    hover_color='Red',
                                    command=add_date)
        cancel_button = ctk.CTkButton(self,
                                    text = 'Next',
                                    fg_color='Blue',
                                    hover_color='Red',
                                    command=lambda: controller.show_frame(dashboard_screen))
        enter_button.pack()
        cancel_button.pack()
        new_date_label.pack()
        input_entry.pack()
        input_frame.pack()
        
class save_state(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
        save_state_label = ctk.CTkLabel(self,
                                      text = 'Checking')
        cancel_button = ctk.CTkButton(self,
                                    text = 'Next',
                                    fg_color='Blue',
                                    hover_color='Red',
                                    command=lambda: controller.show_frame(dashboard_screen))
        save_button = ctk.CTkButton(self,
                                    text = 'Next',
                                    fg_color='Blue',
                                    hover_color='Red',
                                    command=lambda: controller.show_frame(dashboard_screen))
        cancel_button.pack()
        save_state_label.pack()
        save_button.pack()
class summary_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
class productivity_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self,parent)
app = App('FocuSync', (1000, 600))
app.mainloop()