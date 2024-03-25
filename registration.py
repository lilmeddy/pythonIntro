user =[]

# while isNotLoggedIn:
for users in range(2):   
    userName =input("Enter your username\n")
    for i in user:
       while i[0] == userName:
            print("UserName taken")
            userName= input("Enter your user name\n")
    lastName,password = input("Enter your last name\n"),input("Enter your password\n")
    while len(password) < 10 :
        print("Password must be greater than 10 characters");password = input("Enter your password\n")

    user.append([userName,lastName,password])
    
    print(user)

logged =[]

print("Let's login and do some hehehe");username =input("Enter your user name\n")
for i in user:
    print(user)
    isNotLoggedIn = True
    while i[0] != username:
        print("Invalid username");username = input("Enter your user name\n")
print(user)
passWord= input("Enter your password\n")
if passWord == i[2]:
        logged.append([userName,password]) 
        print(f"The currently logged in user is {logged}")
        isNotLoggedIn = False
else:
    print("invalid password");change = input("forgot password?? Enter yes to change password ")
    if change == "yes":
        i.pop(2)
        newPassword = input("enter new password\n");i.append(newPassword);print(user)  
    



# print(user)

