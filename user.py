from Base import baseclass

class user(baseclass):
    def __init__(self , firstname , lastname , phonenumber , *args , **kwargs):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        super().__init__(*args,*kwargs)


    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"







