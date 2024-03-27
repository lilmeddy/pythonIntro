# firstName = input("What is your first name ")
# lastName = input("What is your last name ")
# accountBalance = input("what is your account balance ")
# accountNumber = input("what is your account number ")
# print(firstName.capitalize())
# print(firstName.upper())
# print(firstName.lower())

# print(f"Hi {firstName.capitalize()} {lastName.capitalize()}.\nYour Account balance is ${accountBalance}\nYour Account Number is {accountNumber}")
# print(f'''Hi {firstName.capitalize()} {lastName.capitalize()}.
# Your Account balance is ${accountBalance}
# Your Account N2umber is {accountNumber}''')

# Assignment ask student about their scores in science, math and english exam
# Ask for their name, print admission number and find the mean score and write your average score is

# firstName,lastName = input("What is your first name "),input("What is your last name ")
# math = int(input(f'Dear {firstName} {lastName} enter your score in maths exam '))
# science = int(input(f'Dear {firstName} {lastName} enter your score in science exam '))
# english = int(input(f'Dear {firstName} {lastName} enter your score in english exam '))
# add = math + science + english
# mean = add/3
# print(f'''Dear {firstName.capitalize()} {lastName.capitalize()}
# Congratulation you have been offered admission into our University 
# With an average score of {mean}.''') 

# product1, price1 = input("What did customer buy "),int(input(f"Enter the amount paid for  "))
# product2, price2 = input("What did customer buy "),int(input(f"Enter the amount paid for  "))
# product3, price3 = input("What did customer buy "),int(input(f"Enter the amount paid for  "))
# total = price1 + price2 + price3
# print(f'''
# Product Price
# {product1}  ${price1}
# {product2}  ${price2}
# {product3}  ${price3}
# Totals ${total}
# ''')

# a = 10
# b = 2
# c = 5
# d = 7
 
# addition = a + d
# subtraction = a-b
# division = a/b
# multiplication = b*C
# isEven = 201%2
# final =(((a-b)*(a%d))+1)/c
# print(final)

# Comparison
# name = "obafemi"
# name1 = "obafemi"
# # value = False
# theSame =(0.1+0.2 == 0.3)
# print(theSame)

# Boolean

# name = "timi is a good girl"
# print(name.split(" "))

# lists=[1.0, 1, "hi"]
# print(len(lists))
# print(lists[2])
# print(lists[-1])
# print(lists[0])

# tuples              sets               dictionary          lists
# immutable           mutable            mutable             mutable
# orderly             unorderly          orderly             orderly
# symbol()            symbol{}           symbol{}            symbol[]
# eg(1,1.0,"hi")      eg{1,1.0,"hi"}     eg{name:"mede"}     eg[1.0,1,"hii"]
# simple              complex            complex              simple
# acceptDuplicate     doesn'tAccept     doesn'tAcceptKey      accept


# list
eg = ["obafemi", "mayowa", "ibrahim", "mede", "ife", "damola"]
eg.append("hehe")
# to add
eg.extend(["osas",100]) 
# Extend add list together withouth the []
eg.insert(1,"aghedo")
# to edit a particular one sha. then if you replace just insert the index and pop the one you want to delete
eg.pop(eg.index("ibrahim"))
# or
eg.pop(0)
# or 
eg.remove("mayowa")
print(eg)
if "hehe"  in eg :
    eg.remove("hehe")
    eg.append("heh")
else:
    print("I'm not innnn")
# len(list) to find the length
# to clear a list 
# eg =[]

# to reverse a list 
# eg.reverse()


# to insert at a specific index 
eg.insert(1,"mede")


print(eg)

# tuple
eg = ("obafemi", "mayowa", "ibrahim", "mede", "ife", "damola")
# eg.append(10)
print(eg)

# set
eg = {"obafemi", "mayowa", "ibrahim", "mede", "ife", "damola"}
eg.add(10)
print(eg)

# dictionary
eg ={"name":"mede","age":35}
eg["color"]="rebeccapurple"
print(eg)
print(eg["name"])
eg["color"]= 'pink'
print(eg["color"])
print(eg["age"])
del eg["age"]



