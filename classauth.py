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
        username = input("Enter your username")
        for i in self.list :
             print(self.list)
        isNotLoggedIn = True
        while i[0] != username:
            print("Invalid username");username = input("Enter your user name\n")
        print(self.list)
        passWord= input("Enter your password\n")
        if passWord == i[2]:
                self.logged.append([username,passWord]) 
                print(f"The currently logged in user is {self.logged}")
                isNotLoggedIn = False
        else:
            print("invalid password");change = input("forgot password?? Enter yes to change password ")
            if change == "yes":
                i.pop(2)
                newPassword = input("enter new password\n");i.append(newPassword)
                print(f"The currently logged in user is {self.logged} with the password changed to")

        
            
auth()    