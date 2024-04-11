# functions
# if True:
#     print("hello")

def name():
    print("hello")

def name2():
    print("hi")

# for i in range(5):
#     name2()
    
def name3(num):
    for i in range(num):
        print("hello")

# name3(11)
# name = []
# def register():
#     fullname = input("Enter your fullname: ")
#     name.append(fullname)

# for i in range(5):
#     register()
        
def addition(num1, num2):
    return num1+num2

# print(addition(10, 6)) 

age = "timi"

def squareroot(num):
    return num**(1/2)

def factorial(num):
    value = num
    for i in range(num):
        value *= num-i
    return value/num

# print(factorial(5))
# print(squareroot(144))
users = []
def register():
    firstname = input("Enter your firstname ")
    while True:
        if "" in firstname.split(" "):
            print("Wrong input")
            firstname = input("Enter your fullname ")
        else:
            break

    while True:
        phoneNumber = input("Enter your phone number: ")
        if len(phoneNumber) != 11:
            print("Wrong input")
            phoneNumber = input("Enter your phone number: ")
        else:
            val = False
            for i in users:
                if i["phonenumber"] == phoneNumber:
                    print("Number already exists")
                    val = True
            if val == False:
                break

    accountNumber = phoneNumber[1:]

    password = input("Enter your password: ")
    while True:
        if len(password) < 6:
            print("Wrong input")
            password = input("Enter your password: ")
        else:
            break

    comfirmpass = input("Confirm your password: ")
    while password != comfirmpass:
        print("Wrong input")
        comfirmpass = input("Confirm your password: ")

    users.append({
        "firstname": firstname,
        "accountnumber": accountNumber,
        "phonenumber": phoneNumber,
        "password": password,
        "balance": 0
    })
    print("\nRegistration successful")
    startpage()

def login():
    while True:
        phoneNumber = input("Enter your phone number: ")
        password = input("Enter your password: ")
        val = True
        for i in users:
            if i["phonenumber"] == phoneNumber:
                if password == i["password"]:
                    print("\nLogin successful")
                    val = False
        if val == False:
            break
        else:
            print("Incorrect username or password")
    home(phoneNumber)

def home(phoneNumber):
    while True:
        loggedUser = ""
        for i in users:
            if i["phonenumber"] == phoneNumber:
                loggedUser = i
        if loggedUser == "":
            while True:
                opt = input("")
        print(f"\nWelcome back {loggedUser["firstname"].capitalize()}\nYour balance is${loggedUser["balance"]}")
        print("Enter 1 to transfer\nEnter 2 to deposit\nEnter 3 to withdraw\nEnter 4 to logout")
        ans = input("")
        if ans in ["1", "2", "3", "4"]:
            if ans == "1":
                transfer(loggedUser)
            elif ans == "2":
                deposit(loggedUser)
            elif ans == "3":
                withdraw(loggedUser)
            elif ans == "4":
                print("\nLogout successful")
                phoneNumber = ""
                startpage()
        else:
            print("Invalid input")
   
def transfer(loggeduser):
    for i in users:
        if i["phonenumber"] == loggeduser["phonenumber"]:
            continue
        print(i["phonenumber"])
    while True:
        acct = input("Enter account you want to transfer to: ")
        val = False
        for i in users:
            if i["phonenumber"] == acct:
                val = True
        if val == True:
            break
        else:
            print("Wrong account number")
     
    while True:
        bal = input("Enter amount to transfer: ")
        if int(bal) < loggeduser["balance"]:
            print("transfer successful")
            break
        else:
            print("Account balance too low")
            ans = input("Enter 1 to try again and any number to quit\n")
            if ans == "1":
                pass
            else:
                home(loggeduser["phonenumber"])
    
    acct["balance"] += bal
    loggeduser -= bal
    home(loggeduser["phonenumber"])
def deposit(loggeduser):
    for i in users:
        if i["phonenumber"] == loggeduser["phonenumber"]:
            continue
    print(i["phonenumber"])
    acct = int(input("Enter the amount you want to deposit: "))
    loggeduser["balance"] += acct
    print(f"Deposit successful your balance is {loggeduser["balance"]}")
    home(loggeduser["phonenumber"])
def withdraw(loggeduser):
    for i in users:
        if i["phonenumber"] == loggeduser["phonenumber"]:
            continue
    print(i["phonenumber"])
    acct = int(input("Enter the amount you want to deposit: "))
    loggeduser["balance"] -= acct
    print(f"Deposit successful your balance is {loggeduser["balance"]}")
    home(loggeduser["phonenumber"])
    


def startpage():
    print("Welcome to our bank\n")
    print("Enter 1 to register\nEnter 2 to login\nEnter 3 to quit")
    ans = input("")
    if ans in ["1", "2", "3"]:
        if ans == "1":
            register()
        if ans == "2":
            login()

startpage()