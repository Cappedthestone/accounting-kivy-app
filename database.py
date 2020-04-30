


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            ids, username, password = line.strip().split(";")
            self.users[username] = (username, password)

        self.file.close()

    def get_logins(self, username):
        if username in self.users:
            return self.users[username]
        else:
            return -1

   

    def validate(self, username, password):
        if self.get_logins(username) != -1:
            return self.users[username][1] == password
        else:
            return False