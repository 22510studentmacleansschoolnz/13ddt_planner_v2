import json
import os
from models import User

class UserManager:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r') as f:
                user_data = json.load(f)
                return {username: User(username, data['email'], data['password']) 
                        for username, data in user_data.items()}
        return {}

    def save_users(self):
        user_data = {user.username: {'email': user.email, 'password': user.password} 
                     for user in self.users.values()}
        with open('users.json', 'w') as f:
            json.dump(user_data, f)

    def add_user(self, username, email, password):
        self.users[username] = User(username, email, password)
        self.save_users()

    def authenticate(self, username, password):
        return username in self.users and self.users[username].password == password