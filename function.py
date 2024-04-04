# # parameterize and none paramenterize

# # non-parameterize 

# def name():
#     print("hello")    
# name()
# for i in range(5):
#     name()
# #parameterize

# def name3(name):
#     print(name)
    
# name3("shade")
# def name3(num):
#     for i in range(num):
#         print("mede")
# name3(11)
# #SHADE is the argument
# name =[]
# def register():
#     fullname = input("enter your name ")
#     name.append(fullname)
    
# for i in range(5):
#     register()
    
# def addition(num1,num2):
#     return num1+num2

# print(addition(1,7))


def factorial(num):
    res = 1
    for i in range(1,num+1):
         res *= i 
    return res
print(factorial(4))
