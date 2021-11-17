
class user():
    def __init__(self,username,id):
        self.username = username
        self.id = id

class dj(user):
    def __init__(self,username,id,bio,genres):
        super().__init__(username,id)
        self.bio = bio
        self.genres = genres
        

class customer(user):
    def __init__(self,username,id,company):
        super().__init__(username,id)
        self.company = company

class admin(user):
    def __init__(self,username,id,permissions):
        super().__init__(username,id)
        self.permissions = permissions