# assignment/ project 
# register login transfer deposit withdraw
# registration firstname last name account number phone number 
# registration 
first = []
middle =[]
last = []
accoutBalance=[]
fixedBalance = 50000
phone = []
username = []
user =[]
login =[]
for i in range(2):
    inp = input("Hi dear thanks for choosing lilmeddy bank\nBanking with us for the first time?\nEnter 1 to register\nAlready have an account?\nEnter 2 to login\nEnter either 1 or 2 entering any other thing would terminate your program and you'll have to start again ")
    if inp == "1" :
        fixedBalance +=50000;accoutBalance.append(fixedBalance);firstName = input("Enter your first name (compulsory)\n").capitalize()
        new = False
        while new == False:
            for i in firstName.split(" "):
                if i != "":
                    new = i
            if new == False: 
                firstName = input("You don't have sense after saying compulsory you are typing rubbish\nEnter your firstname mumu\n ")
        first.append(new)
        middleName = input("Enter your middle name (optional)\n").capitalize();middle.append(middleName)
        lastName = input("Enter your last name (compulsory)\n").capitalize();stress = False
        while stress == False:
            for i in lastName.split(" "):
                if i != "":
                    stress = i
            if stress ==False: 
               lastName = input("You don't have sense can't you see compulsory \nEnter your last name mumu\n").capitalize()
        last.append(stress);starts = ["9","8","7"];sec = ["0","1"]
        phoneNumber = input("Enter your phone number\n+234 ");num = False 
        while num == False:
            for i in phone:
                while i == phoneNumber:
                    phoneNumber = input("Phone number taken\nEnter your phone number\n+234 ")
            for i in phoneNumber.split(" "):
                if i != "" and i[0] in starts and i[1] in sec and len(i)==10  :
                    num = i
                if num == False:
                    phoneNumber = input("All nigerians phone number +234 (and should start with 9,8 or 7 and the second value should be 0 or 1) and 10 digits\nEnter your phone number \n+234 ")
        phone.append(num)
    user.extend([first,middle,last,accoutBalance,phone])
    print("Registration successful now let's set your login details you'll pick a username for yourself and we have some suggested user name if needed and you'll also set your password and we can suggest for you also")
    accountNum =input("Enter your accountNumber (Your account number is your phone number and password )\n")
    found = False
    while found == False:
        if accountNum in phone:
            indexPhone = phone.index(accountNum);suggested= first[indexPhone][:4] + last[indexPhone][:3].lower() + phone[-1][2:9:3]
            userName = input(f"Enter a password\nSuggested password {suggested}\n")
        if found == False:
            accountNum =input("Account Not found\nEnter your accountNumber (Your account number is your phone number and password )\n")
    login.append[accountNum,userName]
    print(login)