class User:
  def __init__(self, username, email, password):
      self.username = username
      self.email = email
      self.password = password

class Task:
  def __init__(self, date, time, description):
      self.date = date
      self.time = time
      self.description = description

  def __str__(self):
      return f"{self.date}: {self.time} - {self.description}"