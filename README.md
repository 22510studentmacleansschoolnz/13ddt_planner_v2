# Daily Planner

This simple daily planner app, built with Python and Tkinter, helps you stay organized. Here's what you can do:

- **Sign Up and Sign In**: Create an account and log in securely.
- **Manage Tasks**: Add, remove, and modify tasks for specific dates.
- **Take Notes**: Create and save daily notes.
- **Export/Import Data**: Save your planner data to JSON or CSV files and load it back in.
- **Switch Users**: Easily switch between different user accounts.

## Features

### User Authentication
- Secure login with password protection.
- User data stored in a JSON file (`users.json`).

### Planner Functionality
- Calendar widget for selecting dates.
- Time dropdown for specifying task times.
- Listbox to display and manage tasks.
- Notes section with a text editor for capturing notes.

### Data Management
- Tasks and notes are saved in separate JSON files per user (e.g., `username_tasks.json`, `username_notes.txt`).
- Export data to JSON or CSV files for backup or sharing.
- Import data from JSON or CSV files to restore or merge data.

### User-Friendly Interface
- Simple and intuitive GUI designed with Tkinter.
- Clear layout and easy-to-use controls.

## Installation

### Requirements
- Python 3.x
- Tkinter (usually included with Python)
- `tkcalendar` library: `pip install tkcalendar`

### Download the Code
- Download or clone this repository.

### Run the Program
1. Navigate to the directory containing the `main.py` file.
2. Execute the command: `python main.py`

## Usage

### Sign Up (if new)
1. Click the "Sign Up" button on the sign-in page.
2. Enter your email, username, and password.
3. Confirm your password.
4. Click "Create Account."

### Sign In
1. Enter your username and password.
2. Click "Sign In."

### Planner Page
- **Calendar**: Use the calendar to select a date.

#### Task List
- **Add tasks**: Enter a task description and click "Add Task."
- **Remove tasks**: Select them and click "Remove Task."
- **Modify tasks**: Select them and click "Modify Task."

### Notes
- Enter notes in the text area.
- Click "Save Notes" to save your notes.

### Export/Import Data
- Click the "Export Data" button to save your tasks and notes to a file.
- Click the "Import Data" button to load data from a file.

### Switch Users
1. Click the "Switch User" button to view a list of users.
2. Select a user and enter their password.
3. The application will switch to the selected user's planner.

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
