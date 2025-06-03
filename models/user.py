
class User:
    def __init__(self, username:str):
        self.chips = 1000
        self.username = username

    def add_chips(self):
        self.chips = 1000

    def remove_chips(self, count):
        self.chips -= count

    def get_chips(self):
        return self.chips

    def __repr__(self):
        return {'username': self.username, 'chips': self.chips}
