class Customer:

    def __init__(self, id, fname, lname, adress, mobile):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.adress = adress
        self.mobile = mobile

    def __str__(self):
        return f'{self.id}, {self.fname}, {self.lname}, {self.adress}, {self.mobile}'

    def __repr__(self):
        return f'{self.id}, {self.fname}, {self.lname}, {self.adress}, {self.mobile}'





