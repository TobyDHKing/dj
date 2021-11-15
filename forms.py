
class LoginForm():
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def validateUsername(self):
        length = len(self.username)
        print(length , "username")
        if (not(length > 4)or not(length < 25)):
            return False
        else:
            return True

    def validatePassword(self):
        length = len(self.password)
        print(length , "password")
        if (not(length > 4)and not(length > 25)):
            print(length)
            return False
        else:
            return True
    
    def validateAll(self):
        if (self.validatePassword() and self.validateUsername()):
            return True
        else:
            return False