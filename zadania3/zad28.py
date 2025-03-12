class User:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        self.users[username] = password

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Zalogowano pomyślnie")
        else:
            print("Nieprawidłowe dane logowania")

user = User()
user.register("admin", "admin123")
user.login("admin", "admin123")