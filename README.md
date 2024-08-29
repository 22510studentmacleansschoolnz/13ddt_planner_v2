Daily Planner
This simple daily planner app, built with Python and Tkinter, helps you stay organized. Here's what you can do:
Sign Up and Sign In: Create an account and log in securely.
Manage Tasks: Add, remove, and modify tasks for specific dates.
Take Notes: Create and save daily notes.
Export/Import Data: Save your planner data to JSON or CSV files and load it back in.
Switch Users: Easily switch between different user accounts.
Features
User Authentication:
Secure login with password protection.
User data stored in a JSON file (users.json).
Planner Functionality:
Calendar widget for selecting dates.
Time dropdown for specifying task times.
Listbox to display and manage tasks.
Notes section with a text editor for capturing notes.
Data Management:
Tasks and notes are saved in separate JSON files per user (e.g., username_tasks.json, username_notes.txt).
Export data to JSON or CSV files for backup or sharing.
Import data from JSON or CSV files to restore or merge data.
User-Friendly Interface:
Simple and intuitive GUI designed with Tkinter.
Clear layout and easy-to-use controls.
Installation
Requirements:
Python 3.x
Tkinter (usually included with Python)
tkcalendar library: pip install tkcalendar
Download the code:
Download or clone this repository.
Run the program:
Navigate to the directory containing the main.py file.
Execute the command: python main.py
Usage
Sign Up (if new):
Click the "Sign Up" button on the sign-in page.
Enter your email, username, and password.
Confirm your password.
Click "Create Account."
Sign In:
Enter your username and password.
Click "Sign In."
Planner Page:
Calendar: Use the calendar to select a date.
Task List:
Add tasks by entering a task description and clicking "Add Task."
Remove tasks by selecting them and clicking "Remove Task."
Modify tasks by selecting them and clicking "Modify Task."
Notes:
Enter notes in the text area.
Click "Save Notes" to save your notes.
Export/Import Data:
Click the "Export Data" button to save your tasks and notes to a file.
Click the "Import Data" button to load data from a file.
Switch Users:
Click the "Switch User" button to view a list of users.
Select a user and enter their password.
The application will switch to the selected user's planner.
Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests.
License
This project is licensed under the MIT License. 
