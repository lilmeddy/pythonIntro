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
        phoneNumber = input("Enter your phone number: ")
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
             print(self.list)
        while i[0] != username:
            print("Invalid username");username = input("Enter your full name: ")
        print(self.list)
        passWord= input("Enter your password\n")
        while passWord != i[2]:
            passWord= input("Invalid password\nEnter your password: ")
        self.logged.append([username,passWord]) 
        print(f"The currently logged in user is {self.logged}")
       

        
            
auth()    