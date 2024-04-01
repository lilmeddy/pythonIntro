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
for i in range(3):
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
                amount = accoutBalance[indexPhone]
                userName = input(f"Enter a username\nSuggested user name {suggested}\n")
                for i in login:
                    while i[1] == userName:
                            print("UserName taken")
                            userName= input("Enter your user name\n")
                transactPin = accountNum[:5]
                print(f"Dear {userName} your transaction pin is {transactPin}")
                break
            else:
              accountNum =input("Invalid\nEnter your accountNumber (Your account number is your phone number and password )\n")  
        login.append([accountNum,userName,amount,transactPin])
    if inp =="2":
        maxAttempts = 3
        attempts = 0
        while attempts < maxAttempts:
            username = input("Enter your username: ")
            password = input("Enter your password (account number): ")

            userFound = False
            for i in login:
                if i[1] == username and i[0] == password:
                    userFound = True
                    check = input(f"Welcome {username} thanks for banking with us\nWhat will you like to do?\nEnter 1 to check your balance 2 to withdraw and 3 to transfer 4 to buy airtime 5 to log out\n")
                    if check == "1":
                      print(f"Your current balance is {i[2]}")

                    elif check == "2":
                        amount = float(input("Enter the amount to withdraw: "))
                        if amount <= i[2]:
                            i[2] -= amount
                            transactionPin = input("Enter your transaction pin: ")
                            if transactionPin == i[3]:
                                i[2] -= amount
                                print(f"Withdrawal successful. Your new balance is {i[2]}")
                            else:
                               print("Incorrect transaction pin. Withdrawal cancelled.")
                        else:
                            print(f"Insufficient balance. ¥our balance is {i[2]}")

                    elif check == "3":
                        receiverPhone = input("Enter the receiver's phone number: ")
                        amount = float(input("Enter the amount to transfer: "))
                        if amount <= i[2]:
                            transactionPin = input("Enter your transaction pin: ")
                            if transactionPin == i[3]:
                                for receiverInfo in login:
                                    if receiverInfo[0] == receiverPhone:
                                        receiverInfo[2] += amount
                                        print(f"You are about to send {amount} to {receiverInfo[1]}")
                                        i[2] -= amount
                                        print(f"Transfer successful.Your balance is {i[2]}")
                                        break
                                else:
                                    print("Receiver not found.")
                            else:
                                 print("Incorrect transaction pin. Transfer cancelled.")
                        else:
                                print(f"Insufficient balance.Your balance is {i[2]}")

                    elif check == "4":
                        amount = float(input("Enter the amount of airtime to buy: "))
                        if amount <= i[2]:
                            i[2] -= amount
                            transactionPin = input("Enter your transaction pin: ")
                            if transactionPin == i[3]:
                                print(f"Airtime purchase to the phone number in this account 0{i[0]} successful.Your balance new is {i[2]}")
                            else:
                                 print("Incorrect transaction pin. Airtime purchase cancelled.")
                        else:
                            print(f"Insufficient balance.Your balance is {i[2]}")

                    elif check == "5":
                        print("Logging out.")
                        break  

                    else:
                        print("Invalid choice.")

                    break 
            if not userFound:
                attempts += 1
                print("Invalid username or password. Please try again.")    
        else:
         print("Maximum login attempts reached. Exiting program.")
   
            
            
            