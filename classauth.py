class auth:
    def __init__(self) -> None:
        self.list = []
        self.logged =[]
        self.reg()
        self.log()
    def reg(self):
        name = input("Enter your full name: ")
        phoneNumber = input("Enter your phone number: ")
        password = input("Enter your password: ")
        self.list.append([name, phoneNumber, password])
        print("Enter  ")
    def log(self):
        username = input("Enter your username: ")
        for i in self.list :
             print(self.list)
        while i[0] != username:
            print("Invalid username");username = input("Enter your user name: ")
        print(self.list)
        passWord= input("Enter your password\n")
        while passWord != i[2]:
            passWord= input("Invalid password\nEnter your password: ")
        self.logged.append([username,passWord]) 
        print(f"The currently logged in user is {self.logged}")
       

        
            
auth()    