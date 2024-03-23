

for users in range(1):   
    userName =input("Enter your username\n")
    for i in user:
       while i[0] == userName:
            print("UserName taken")
            userName= input("Enter your user name\n")
    lastName,password = input("Enter your last name\n"),input("Enter your password\n")
    while len(password) < 10 :
        print("Password must be greater than 10 characters")
        password = input("Enter your password\n")

    user.append([userName,lastName,password])
# login 
    print(user)
    for i in user:
       print("Let's login and do some hehehe")
       username =input("Enter your user name\n")
    #    while i[0] != userName:
    #         print("Invalid username")
    #         userName= input("Enter your user name\n")
       passWord= input("Enter your password\n")
       print(user)
       if i[0] == username:
           print(i)
       while passWord != i[2]:
            #  print("Login Successful")
           change = input("forgot password?? Enter yes to change password ")
           if change == "yes":
             i.pop(2)
             print(user) 
           newPassword = input("enter new password")
           i.insert(2, newPassword)
           #testing
        # print(user)
print(user)

# erfghjkl.,mnfdsdfghjksxcvb

# print(user)
# frtgyhujnmkwdq

