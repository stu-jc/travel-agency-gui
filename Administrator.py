class Administrator:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    def get_name(self):
        return self.name

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password
        