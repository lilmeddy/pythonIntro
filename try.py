# try:
#     int(input("Enter a number "))
# except:
#     print("There's an error here")
# else:
#     print("There is no error here")
# finally:
#     print("Hehehe")
# while True:   
#     try:
#         int(input("Enter a number "))
#     except:
#         print("There's an error here")
#     else:
#         print("There is no error here")
#         break

while True:   
    try:
        int(input("Enter a number "))
        try:
            var1 = 2 + "2"
        except:
            print("You can't add both together ")
    except:
        print("There's an error here")
    else:
        print("There is no error here")
        break
    