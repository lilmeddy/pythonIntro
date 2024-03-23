# assignment1
# create an origin list of your classmates
# ask for the names of 5 student add each of them to a list
# merge both list together 
# ask for a name the user want to search for 
# print the index of the name


# the original list of my matess
# classNames = ["Osamede", "Obafemi", "Damola","Duro","Ibrahim"]
# firstName, secondName,thirdName,fourthName,fithName = input("Enter your name: "),input("Enter your name: "),input("Enter your name: "),input("Enter your name: "),input("Enter your name: ")
# classNames.extend([firstName, secondName, thirdName,fourthName,fithName])
# print(classNames.index(input("Search for a name: ")))
#  slicing doesn't give the end but the one before the last number if you want it to give you the last number then use 0:len(className) or [0:]
# print(classNames[3:9:2])
# the third one like 2 is at a skip of one you can increase the skip sha

# should print 0-8 instead 



# assignment2
# ask a user for input and check if it is even if it is even print is even else no 
# num = int(input("Enter your yeye number jare: "))
# if num%2 == 0 :
#     print(f"The number you provided is {num}. Lucky you {num} is an even number")
# else:
#     print(f"The number you provided is {num}. Unlucky you {num} is an odd number")

# numbers =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(numbers[1::2])

listt =["obafemi", "damolaaaaaaaaaaaaaaaaaa"]
for i in listt :
    if len(i) > 10 :
        print(f"{i} is greater than 10 character")

inp = input("Enter your password: ")
while len(inp) < 10 :
    print("Password must be greater than 10 characters")
    inp = input("Enter your password: ")



 