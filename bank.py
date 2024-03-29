# assignment/ project 
# register login transfer deposit withdraw
# registration firstname last name account number phone number 
# registration 
first = []
middle =[]
last = []
accoutBalance=[]
phone = []
user =[]
for i in range(2):
    firstName = input("Enter your first name (compulsory)\n").capitalize()
    new = False
    while new == False:
        for i in firstName.split(" "):
            if i != "":
                new = i
        if new == False: 
            firstName = input("You don't have sense after saying compulsory you are typing rubbish\n Enter your firstname mumu\n ")
    first.append(new)
    middleName = input("Enter your middle name (optional)\n").capitalize()
    middle.append(middleName)
    lastName = input("Enter your last name (compulsory)\n").capitalize()
    stress = False
    while stress == False:
        for i in lastName.split(" "):
            if i != "":
                stress = i
        if stress ==False: 
           lastName = input("You don't have sense can't you see compulsory \nEnter your last name mumu\n").capitalize()
    last.append(stress) 
    accoutBalance *=2
    starts = ["9","8","7"]
    sec = ["0","1"]
    phoneNumber = input("Enter your phone number\n+234 ")
    num = False 
    while num == False:
        for i in starts:
            val = phoneNumber.split()
            if phoneNumber.startswith(i) and val[1] in sec and phoneNumber.len:
                num = phoneNumber
                num == True
            if num == False:
               phoneNumber = input("All nigerians phone number +234 (and should start with 9,8 or 7 and the second value should be 0 or 1)\nEnter your phone number \n+234 ")
    phone.append(num)
            
    user.extend([first,last,accoutBalance,phone])
    

print(user)