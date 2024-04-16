class auth:
    def __init__(self) -> None:
        self.list = []
        self.reg()
        self.log()
    def reg(self):
        name = input("Enter your full name: ")
        phoneNumber = input("Enter your phone number: ")
        password = input("Enter your password: ")
        self.list.append([name, phoneNumber, password])
        print(self.list)
    def log(self):
        pass 
auth()    