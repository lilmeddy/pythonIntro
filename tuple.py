# tuple is used for security it is immutable and ordered 
# casting 
fruits = ("apple","mango","pineapple")
newTuple = list(fruits)
print(newTuple.append("carrot"))
print(newTuple)
print(tuple(newTuple))
# myU|Lr'/ry")
# (first,second) = fruits
(first, *second, third) = fruits #note this will print to the end
print(second)
print(third)

# create a program to ask for all names(first, *middle*,last)  of five students group all the first name in a list middle in a list and last name in a list 
first = []
middle =[]
last = []
for i in range(2):
    firstName = input("Enter your first name (compulsory)\n").capitalize()
    new = False
    while new == False:
        for i in firstName.split(" "):
            if i != "":
                new = i
        for i in range(9):
            if new ==False and new : 
                firstName = input("You don't have sense after saying compulsory you are typing rubbish\n Enter your firstname mumu\n ")
        
    print(new)
    first.append(new)
    middleName = input("Enter your middle name (optional)\n").capitalize()
    middle.append(middleName)
    lastName = input("Enter your last name (compulsory)\n").capitalize()
    stress = False
    while lastName == "":
        lastName = input("You don't have sense can't you see compulsory \nEnter your last name mumu\n").capitalize()
    last.append(lastName) 
print(first);print(middle);print(last)
# student records
# 1. duro duro duro