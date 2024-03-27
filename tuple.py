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
    firstName = input("Enter your first name (compulsory)\n")
    while firstName == "":
        firstName = input("You don't have sense can't you see compulsory \nEnter your first name mumu\n")
    first.append(firstName)
    print(first)
    middleName = input("Enter your middle name (optional)\n")
    if middleName == "":
        middleName = "NIL"
    middle.append(middleName)
    print(middle)
    lastName = input("Enter your last name (compulsory)\n")
    while lastName == "":
        lastName = input("You don't have sense can't you see compulsory \nEnter your last name mumu\n")
    last.append(lastName)
    print(last)