# range function 
# passing 1 parameter i.e (starts from zero ends at the parameter specified without returning the parameter)
# for num in range(10):
#     print(num)

# passing 2 parameter i.e (starts fron zero and ends the parameter specified without returning the parameter )
# for num in range (4,10):
#     print(num)

# passing 3 parameter i.e (starts from first paramter end at second without returning the second at a step of the third-1 e.g 2 step will be 1 )
# for num in range (4,10,2):
#     print(num) 

# numbers =[]
# for num in range(3):
#     numbers.append(input("Enter a number: "))
# print(numbers)

# listt = ["duro","duro123","mide","mide123"]
# username =listt[0:len(listt):2]
# password =listt[1:len(listt):2]

# print(listt)

# for i in range(0,len(listt)):
#     if i%2 == 0:
#         username.append(listt[i])
#     else:
#         password.append(listt[i])

# print(username)
# print(password)

# num =[0,1,2,3,4,5,6,7,8,5,3,2,4,5,6,,8,6,43,354657]
# generate a list of 1-100 and get all the prime number 
primeNum=[]
for i in range(2,101,2):
   primeNum.append(i)
print(primeNum)
# or 
# for num in range(1,101):
#     if num >1 :
#         prime = True
#         for i in range(2,num):
#             if num%i == 0:
#               prime = False
#         if prime:
#            print(num,end=',')
         #   primeNum.append(num)
# print(primeNum)
# or 
# for i in range(1,20):
#     if i%2 != 0:
#         continue
#     primeNum.append(i)
# print(primeNum)
# calculator 
num1,num2 = int(input("Enter first number ")),int(input("Enter second number "))
sign = int(input("Enter:\n1 to add\n2 to subtract\n3 to multiply\n4 to find the modulus\n5 to divide\n6 to find exponential\n"))
if sign == 1:
   print(num1+num2)
elif sign ==2:
   print(num1-num2)
elif sign ==3:
   print(num1*num2)
elif sign ==4:
   print(num1%num2)
elif sign ==5:
   print(num1/num2)
elif sign ==6:
   print(num1**num2)
else:
   print("Math error")
   sign = int(input("Enter:\n1 to add\n2 to subtract\n3 to multiply\n4 to find the modulus\n5 to divide\n6 to find exponential\n"))
               
               
