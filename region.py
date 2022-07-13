from Base import baseclass


class region(baseclass):
    def __init__(self,name,*args,**kwargs):
        self.name = name
        super().__init__(*args,**kwargs)


