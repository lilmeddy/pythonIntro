users =[]

for user in range(1):   
    user_name =input("Register - Enter your username\n")
    for i in users:
       while i["user_name"] == user_name:
            print("Username taken")
            user_name= input("Enter a different username\n")
    last_name,password = input("Enter your last name\n"),input("Enter your password\n")
    while len(password) < 8 :
        print("Password must be greater than 8 characters")
        password = input("Enter your password\n")

    myUser = dict(user_name=user_name, last_name=last_name, password=password)
    users.append(myUser)

# login 
    print("Let's login and do some hehehe")
    user_name =input("Enter your username\n")
    for i in users:
        if i["user_name"] == user_name:
            print("user found!")
            password= input("Enter your password\n")
            if i["password"] == password:
                print("Login Successful")
                break
            else :    
                change = input("forgot password?? Enter yes to change password ")
                if change == "yes":
                    new_password = input("enter new password\n")
                    i["password"] = new_password
                    print(f"your new info: {i}")
                    break
        else:
            print("User not found")
        
           
        
print(users)



#  logged =[]
# # login 
# # print(user)
#     print("Let's login and do some hehehe");username =input("Enter your user name\n")
#     for i in user:
#        while i[0] != username:
#             print("Invalid username");username = input("Enter your user name\n")
#     passWord= input("Enter your password\n")
#     while passWord == i[2]:
#          logged.append([userName,password]) 
#          print(f"The currently logged in user is {logged}")
#     else:
#         print("invalid password");change = input("forgot password?? Enter yes to change password ")
#         if change == "yes":
#             i.pop(2)
#             newPassword = input("enter new password");i.append(newPassword) ;print(user)  
    


# # print(user)


