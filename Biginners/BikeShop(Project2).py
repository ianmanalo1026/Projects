import string

class Person:
    
    def __init__(self):
        self.name = None
        self.gender = None
        self.address = None
        self.id = None
        self.ref_num = None
        
    def generate_reference_id(self):
        random_password = ""
        raw_password = list(string.ascii_lowercase)
        raw_password.extend(list(string.ascii_uppercase))
        raw_password.extend(list(string.digits))

        length = int(12)
        for x in range(length):
            random_password += random.choice(raw_password)
            self.ref_num = random_password
        
        
    def get_info(self):
        self.name = input("Enter Your Name: ")
        self.gender = input("Enter Your Gender: ")
        self.address = input("Enter Your Address: ")
        self.id = input("Enter Your ID: ")
        self.generate_reference_id()
        
    
class Bike(Person):

        def __init__(self):
            super().__init__()
            self.num_bike = 50
            
        def check_bike(self):
            return f"Remaining number of bike is {self.num_bike}"
        

    
class BikeShop(Bike):
    
    def __init__(self):
        super().__init__()
        
    def borrow_bike(self):
        self.get_info()
        checker = int(input("How many bikes would you like to borrow? "))
        self.num_bike -= checker
    
    def return_bike(self):
        self.num_bike += 1
        
        
        
        
x = BikeShop()

x.check_bike()