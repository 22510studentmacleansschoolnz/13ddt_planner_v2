import os

class NotesManager:
    def __init__(self, username):
        self.username = username

    def load_notes(self):
        filename = f'{self.username}_notes.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return f.read()
        return ""

    def save_notes(self, notes):
        with open(f'{self.username}_notes.txt', 'w') as f:
            f.write(notes)