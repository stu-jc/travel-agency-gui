from Administrator import Administrator

class Administrators:
    def __init__(self):
        self.administrators = []
    
    def has_administrator(self, username, password):
        for a in self.administrators:
            if a.login == username and a.password == password:
                return True
            else:
                pass
        #throw error
    
    def get_administrator(self, username, password):
        for a in self.administrators:
            if a.login == username and a.password == password:
                return a
        #throw error

    def insert_dummy_data(self):
        self.administrators.append(Administrator("The Best", " ", " "))
        self.administrators.append(Administrator("Legend", "L", "notsecure"))
        self.administrators.append(Administrator("Boss", "Recruiter", "hirejosh"))
        self.administrators.append(Administrator("Random Person", "rp", "01"))
        self.administrators.append(Administrator("Captain Obvious", "cap", "1234"))
        self.administrators.append(Administrator("Baron von Banter", "bvb", "hirejosh"))
        self.administrators.append(Administrator("HR Hero", "hrh", "hirejosh"))
        self.administrators.append(Administrator("Recruiting Rockstar", "rr", "hirejosh"))
        self.administrators.append(Administrator("People Person", "pp", "hirejoshuachelashaw"))
        self.administrators.append(Administrator("Talent Whisperer", "youshould", "hireme"))
        self.administrators.append(Administrator("Hiring Guru", "hg", "hirejosh"))


