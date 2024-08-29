import tkinter as tk
from tkinter import messagebox, ttk, simpledialog, filedialog
from tkcalendar import Calendar
import re
from user_manager import UserManager
from task_manager import TaskManager
from notes_manager import NotesManager
from data_manager import DataExporter, DataImporter
from models import Task

class DailyPlannerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Daily Planner")
        self.master.geometry("800x600")

        self.user_manager = UserManager()
        self.current_user = None
        self.task_manager = None
        self.notes_manager = None

        self.create_signin_page()

    def create_signin_page(self):
        self.signin_frame = tk.Frame(self.master)
        self.signin_frame.pack(expand=True, fill='both')

        tk.Label(self.signin_frame, text="Username:").pack(pady=(20, 5))
        self.username_entry = tk.Entry(self.signin_frame)
        self.username_entry.pack()

        tk.Label(self.signin_frame, text="Password:").pack(pady=(10, 5))
        self.password_entry = tk.Entry(self.signin_frame, show="*")
        self.password_entry.pack()

        tk.Button(self.signin_frame, text="Sign In", command=self.sign_in).pack(pady=(20, 0))
        tk.Button(self.signin_frame, text="Sign Up", command=self.create_signup_page).pack(pady=(10, 0))

    def create_signup_page(self):
        self.signin_frame.destroy()
        self.signup_frame = tk.Frame(self.master)
        self.signup_frame.pack(expand=True, fill='both')

        tk.Label(self.signup_frame, text="Email:").pack(pady=(20, 5))
        self.email_entry = tk.Entry(self.signup_frame)
        self.email_entry.pack()

        tk.Label(self.signup_frame, text="Username:").pack(pady=(10, 5))
        self.new_username_entry = tk.Entry(self.signup_frame)
        self.new_username_entry.pack()

        tk.Label(self.signup_frame, text="Password:").pack(pady=(10, 5))
        self.new_password_entry = tk.Entry(self.signup_frame, show="*")
        self.new_password_entry.pack()

        tk.Label(self.signup_frame, text="Confirm Password:").pack(pady=(10, 5))
        self.confirm_password_entry = tk.Entry(self.signup_frame, show="*")
        self.confirm_password_entry.pack()

        tk.Button(self.signup_frame, text="Create Account", command=self.create_account).pack(pady=(20, 0))
        tk.Button(self.signup_frame, text="Back to Sign In", command=self.back_to_signin).pack(pady=(10, 0))

    def back_to_signin(self):
        self.signup_frame.destroy()
        self.create_signin_page()

    def create_account(self):
        email = self.email_entry.get()
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email address")
            return

        if not re.match(r"^[a-zA-Z0-9]{3,20}$", username):
            messagebox.showerror("Error", "Username must be 3-20 alphanumeric characters")
            return

        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        self.user_manager.add_user(username, email, password)
        messagebox.showinfo("Success", "Account created successfully!")
        self.back_to_signin()

    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.user_manager.authenticate(username, password):
            self.current_user = username
            self.task_manager = TaskManager(username)
            self.notes_manager = NotesManager(username)
            self.signin_frame.destroy()
            self.create_planner_page()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def logout(self):
        self.current_user = None
        self.task_manager = None
        self.notes_manager = None
        self.planner_frame.destroy()
        self.create_signin_page()

    def create_planner_page(self):
        self.planner_frame = tk.Frame(self.master)
        self.planner_frame.pack(expand=True, fill='both')

        self.create_top_frame()
        self.create_left_frame()
        self.create_right_frame()

    def create_top_frame(self):
        top_frame = tk.Frame(self.planner_frame)
        top_frame.pack(side='top', fill='x')

        tk.Button(top_frame, text="Logout", command=self.logout).pack(side='right', padx=10, pady=10)
        tk.Button(top_frame, text="Switch User", command=self.show_user_list).pack(side='right', padx=10, pady=10)
        tk.Button(top_frame, text="Export Data", command=self.export_data).pack(side='right', padx=10, pady=10)
        tk.Button(top_frame, text="Import Data", command=self.import_data).pack(side='right', padx=10, pady=10)

    def create_left_frame(self):
        left_frame = tk.Frame(self.planner_frame, width=400)
        left_frame.pack(side='left', fill='both', expand=True)

        self.cal = Calendar(left_frame, selectmode='day', date_pattern='yyyy-mm-dd')
        self.cal.pack(pady=20)

        self.create_time_dropdown(left_frame)
        self.create_task_list(left_frame)
        self.create_task_entry(left_frame)

    def create_time_dropdown(self, parent):
        time_frame = tk.Frame(parent)
        time_frame.pack(pady=10)

        hours = [f"{h:02d}" for h in range(1, 13)]
        minutes = [f"{m:02d}" for m in range(0, 60, 5)]
        am_pm = ["AM", "PM"]

        self.hour_var = tk.StringVar(value="12")
        self.minute_var = tk.StringVar(value="00")
        self.ampm_var = tk.StringVar(value="PM")

        ttk.Combobox(time_frame, textvariable=self.hour_var, values=hours, width=5).pack(side='left', padx=5)
        ttk.Combobox(time_frame, textvariable=self.minute_var, values=minutes, width=5).pack(side='left', padx=5)
        ttk.Combobox(time_frame, textvariable=self.ampm_var, values=am_pm, width=5).pack(side='left', padx=5)

    def create_task_list(self, parent):
        self.task_listbox = tk.Listbox(parent, width=50, height=10)
        self.task_listbox.pack(pady=10)

        for date, tasks in self.task_manager.tasks.items():
            for task in tasks:
                self.task_listbox.insert(tk.END, str(task))

    def create_task_entry(self, parent):
        task_frame = tk.Frame(parent)
        task_frame.pack(fill='x', padx=10)

        self.task_entry = tk.Entry(task_frame, width=40)
        self.task_entry.pack(side='left')

        tk.Button(task_frame, text="Add Task", command=self.add_task).pack(side='left', padx=(10, 5))
        tk.Button(task_frame, text="Remove Task", command=self.remove_task).pack(side='left', padx=(5, 5))
        tk.Button(task_frame, text="Modify Task", command=self.modify_task).pack(side='left', padx=(5, 0))

    def create_right_frame(self):
        right_frame = tk.Frame(self.planner_frame, width=400)
        right_frame.pack(side='right', fill='both', expand=True)

        tk.Label(right_frame, text="Notes:").pack(pady=(20, 5))
        self.notes_text = tk.Text(right_frame, width=50, height=20)
        self.notes_text.pack(pady=10)

        self.notes_text.insert(tk.END, self.notes_manager.load_notes())

        tk.Button(right_frame, text="Save Notes", command=self.save_notes).pack(pady=10)

    def show_user_list(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        user_list_frame = tk.Frame(self.master)
        user_list_frame.pack(expand=True, fill='both')

        if len(self.user_manager.users) <= 1:
            tk.Label(user_list_frame, text="There are no users to show here").pack(pady=20)
        else:
            for username in self.user_manager.users:
                if username != self.current_user:
                    tk.Button(user_list_frame, text=username,
                              command=lambda u=username: self.switch_to_user(u)).pack(pady=5)

        tk.Button(user_list_frame, text="Back to Main Page", command=self.back_to_planner).pack(pady=20)

    def switch_to_user(self, username):
        password = simpledialog.askstring("Password", f"Enter password for {username}:", show='*')
        if self.user_manager.authenticate(username, password):
            result = messagebox.askyesno("Warning", "Please ensure you have saved previous tasks. If you proceed, all unsaved work will be lost. Do you want to continue?")
            if result:
                self.current_user = username
                self.task_manager = TaskManager(username)
                self.notes_manager = NotesManager(username)
                self.back_to_planner()
        else:
            messagebox.showerror("Error", "Incorrect password")

    def back_to_planner(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.create_planner_page()

    def add_task(self):
        description = self.task_entry.get()
        if description:
            date = self.cal.get_date()
            time = f"{self.hour_var.get()}:{self.minute_var.get()} {self.ampm_var.get()}"
            task = Task(date, time, description)
            self.task_manager.add_task(task)
            self.task_listbox.insert(tk.END, str(task))
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task_str = self.task_listbox.get(index)
            date, time_desc = task_str.split(': ', 1)
            time, description = time_desc.split(' - ', 1)
            task = Task(date, time, description)
            self.task_manager.remove_task(task)
            self.task_listbox.delete(index)

    def modify_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task_str = self.task_listbox.get(index)
            date, time_desc = task_str.split(': ', 1)
            time, old_description = time_desc.split(' - ', 1)
            new_description = simpledialog.askstring("Modify Task", "Enter the modified task:", initialvalue=old_description)
            if new_description:
                old_task = Task(date, time, old_description)
                new_task = Task(date, time, new_description)
                self.task_manager.modify_task(old_task, new_task)
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, str(new_task))

    def save_notes(self):
        notes = self.notes_text.get("1.0", tk.END)
        self.notes_manager.save_notes(notes)
        messagebox.showinfo("Success", "Notes saved successfully!")

    def export_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv")])
        if file_path:
            if file_path.endswith('.json'):
                DataExporter.export_json(file_path, self.task_manager.tasks, self.notes_text.get("1.0", tk.END))
            elif file_path.endswith('.csv'):
                DataExporter.export_csv(file_path, self.task_manager.tasks)
            messagebox.showinfo("Success", "Data exported successfully!")

    def import_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv")])
        if file_path:
            if file_path.endswith('.json'):
                tasks, notes = DataImporter.import_json(file_path)
                self.task_manager.tasks = tasks
                self.notes_text.delete("1.0", tk.END)
                self.notes_text.insert(tk.END, notes)
            elif file_path.endswith('.csv'):
                self.task_manager.tasks = DataImporter.import_csv(file_path)
            self.refresh_task_list()
            self.task_manager.save_tasks()
            self.save_notes()
            messagebox.showinfo("Success", "Data imported successfully!")

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for date, tasks in self.task_manager.tasks.items():
            for task in tasks:
                self.task_listbox.insert(tk.END, str(task))