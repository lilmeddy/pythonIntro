class auth:
    def __init__(self) -> None:
        self.list = []
        self.logged =[]
        self.starts =["9","8","7"]
        self.sec =["0","1"]
        self.reg()
        self.log()
    def reg(self):
        name = input("Enter your full name: ")
        new = False
        while new == False:
            for i in name.split(" "):
                if i != "":
                    new = i
            if new == False: 
                name = input("You don't have sense.Enter your name don't stress me: ")
        phoneNumber = input("Enter your phone number: +234 ")
        num = False 
        while num == False:
            for i in phoneNumber.split(" "):
                if i != "" and i[0] in self.starts and i[1] in self.sec and len(i)==10  :
                    num = i
                if num == False:
                    phoneNumber = input("All nigerians phone number +234 (and should start with 9,8 or 7 and the second value should be 0 or 1) and 10 digits\nEnter your phone number \n+234 ")
        password = input("Enter your password: ")
        self.list.append([name, num, password])
    def log(self):
        username = input("Enter your username: ")
        for i in self.list :
            pass
        while i[0] != username:
            print("Invalid username");username = input("Enter your full name: ")
        passWord= input("Enter your password: ")
        while passWord != i[2]:
            passWord= input("Invalid password\nEnter your password: ")
        self.logged.append([username,passWord]) 
        print(f"The currently logged in user is {i[0]}")
       

        
            
auth()    