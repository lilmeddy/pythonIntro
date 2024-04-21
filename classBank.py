class bank:
    def __init__(self) -> None:
        self.users = []
        self.start()
        self.balance = 5000
        self.phone = []
    def start(self):
        print("Welcome to our bank\nEnter 1 to register\nEnter 2 to login\nEnter 3 to quit\n")
        try:
            ans = int(input(""))
            if ans in ["1", "2", "3"]:
                if ans == "1":
                    self.register()
                if ans == "2":
                    self.login()
        except:
            ans = int(input(""))
        else:
            break
    def register(self):
        self.balance +=50000;firstName = input("Enter your first name (compulsory)\n").capitalize();first = False
        while first == False:
            for i in firstName.split(" "):
                if i != "":
                    first = i
            if first == False: 
                firstName = input("Enter your first name (compulsory)\n").capitalize()
        middleName = input("Enter your middle name (optional)\n").capitalize()
        lastName = input("Enter your last name (compulsory)\n").capitalize();last = False
        while last == False:
            for i in lastName.split(" "):
                if i != "":
                    last = i
            if last ==False: 
               lastName = input("Enter your last name (compulsory)\n").capitalize()
        try:
            phoneNumber = int(input("Enter your phone number\n+234 "))
            starts = ["9","8","7"];sec = ["0","1"]
            num = False 
            while num == False:
                for i in self.phone:
                    while i == phoneNumber:
                        phoneNumber = input("Phone number taken\nEnter your phone number\n+234 ")
                for i in phoneNumber.split(" "):
                    if i != "" and i[0] in starts and i[1] in sec and len(i)==10  :
                        num = i
                    if num == False:
                        phoneNumber = input("All nigerians phone number +234 (and should start with 9,8 or 7 and the second value should be 0 or 1) and 10 digits\nEnter your phone number \n+234 ")
        except:
            phoneNumber = input("All nigerians phone number +234 (and should start with 9,8 or 7 and the second value should be 0 or 1) and 10 digits\nEnter your phone number \n+234 ")
        else:
            break
            
         
        
        
        
       

    