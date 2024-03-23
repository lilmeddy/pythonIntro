# assignment 
# ask a user for product he/she want to buy 
# ask for the quantity 
# do step 2 and 3 5 times save it in diction but in every input if the item is already a key in the dictionary print("it already exist")
# after the input show the user he/she cart 
# ask the user if he/she wants to remove a product or checkout or replace or clear cart
# if user enters a remove product set the quantity of that item to zero 
# if the user chooses to replace a product ask for the new item name and quantity and insert it and remove the former 
# if the user clear then clear the dictionary
# if the user checkout extract the key to a list and print a recipt stating the item
# solution 
user = input("Hello Dear customer what is your name "); cart ={}
for prod in range(5):
    product,quantity = input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: "))
    while product in list(cart.keys()) :
       print("Product already exist "); product,quantity = input("Enter new you want to buy: "),int(input("Enter the new quantity of what you want to buy: "))
    else:
       cart[product] = quantity
   
print(f"{user.capitalize()} your cart is\nProduct Item\n{list(cart.keys())[0]} {list(cart.values())[0]}\n{list(cart.keys())[1]} {list(cart.values())[1]}\n{list(cart.keys())[2]} {list(cart.values())[2]}\n{list(cart.keys())[3]} {list(cart.values())[3]}\n{list(cart.keys())[4]} {list(cart.values())[4]}")
editing = int(input("What would you like to do "))
total =list(cart.values())[0] + list(cart.values())[1] + list(cart.values())[2] + list(cart.values())[3] + list(cart.values())[4]
if editing in [1,2,3,4]:
    if editing == 1:
      print(f"{user.capitalize()} your cart is\nProduct Item\n{list(cart.keys())[0]} {list(cart.values())[0]}\n{list(cart.keys())[1]} {list(cart.values())[1]}\n{list(cart.keys())[2]} {list(cart.values())[2]}\n{list(cart.keys())[3]} {list(cart.values())[3]}\n{list(cart.keys())[4]} {list(cart.values())[4]}\n and your total is {total}")
    elif editing == 2:
         newProduct, newItem = input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: ")); cart[newProduct] = newItem; del[editing]
    elif editing == 3:
          cart = {}
    elif editing == 4 :
        newEdit = input("what product would you like to adjust ")
        cart[newEdit] = 0
    else:
       print("invalid input")
else: 
    print("Invalid number pick 1-4")



# product1,quantity1 = input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: "))
# cart[product1] = quantity1
# product2,quantity2 = input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: "))
# if product2 in list(cart.keys()) :
#     print("Product already exist ")
#     question= input("Do you want to change prodouct ")
#     if question == "yes" :
#        productRep, quantityRep = input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: "))
#        if productRep in list(cart.keys()) :
#            print("are you okay why are you repeating products idiot")
#        else :
#            cart[productRep] = quantityRep 
#     else: 
#        print("Continue your shopping")

# else:
#     cart[product2] = quantity2

# product3,quantity3 = input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: "))
# if product3 in list(cart.keys()) :
#     print("Product already exist ")
#     question= input("Do you want to change prodouct ")
#     if question == "yes" :
#        productRep, quantityRep = input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: "))
#        if productRep in list(cart.keys()) :
#            print("are you okay why are you repeating products idiot")
#        else :
#            cart[productRep] = quantityRep 
#     else: 
#        print("Continue your shopping")
       

# else:
#     cart[product3] = quantity3

# product4,quantity4 = input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: "))
# if product4 in list(cart.keys()) :
#     print("Product already exist ")
#     question= input("Do you want to change prodouct ")
#     if question == "yes" :
#        productRep, quantityRep = input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: "))
#        if productRep in list(cart.keys()) :
#            print("are you okay why are you repeating products idiot")
#        else :
#            cart[productRep] = quantityRep 
#     else: 
#        print("Continue your shopping")

# else:
#     cart[product4] = quantity4

# product5,quantity5= input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: "))
# if product5 in list(cart.keys()) :
#     print("Product already exist ")
#     question= input("Do you want to change prodouct ")
#     if question == "yes" :
#        productRep, quantityRep = input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: "))
#        if productRep in list(cart.keys()) :
#            print("are you okay why are you repeating products idiot")
#        else :
#            cart[productRep] = quantityRep 
#     else: 
#        print("Continue your shopping")

# else:
#     cart[product5] = quantity5

# print(f'''
# Your cart is 
# Product Item
# {list(cart.keys())[0]} {list(cart.values())[0]}
# {list(cart.keys())[1]} {list(cart.values())[1]}
# {list(cart.keys())[2]} {list(cart.values())[2]}
# {list(cart.keys())[3]} {list(cart.values())[3]}
# {list(cart.keys())[4]} {list(cart.values())[4]}
#       ''')

# print(f'''
#  Dear user do you want to checkout or replace or clear cart
# To checkout enter 1
# To replace enter 2
# To clear enter 3
# To remove enter 4
# ''')

# editing = int(input("What would you like to do "))
# total =list(cart.values())[0] + list(cart.values())[1] + list(cart.values())[2] + list(cart.values())[3] + list(cart.values())[4]
# if editing in [1,2,3,4]:
#     if editing == 1:
# print(f'''
#             Dear {user} thanks for shopping with us 
#     Your cart is 
#     PRODUCT ITEM
#     {list(cart.keys())[0]} {list(cart.values())[0]}
#     {list(cart.keys())[1]} {list(cart.values())[1]}
#     {list(cart.keys())[2]} {list(cart.values())[2]}
#     {list(cart.keys())[3]} {list(cart.values())[3]}
#     {list(cart.keys())[4]} {list(cart.values())[4]}
#     Your total qualtity is {total}.
# ''')

#     elif editing == 2:
#          newProduct, newItem = input("Enter what you want to buy: "),int(input("Enter the quantity of what you want to buy: "))
#          cart[newProduct] = newItem
#          del[editing]

#     elif editing == 3:
#           cart = {}
   

#     elif editing == 4 :
#         newEdit = input("what product would you like to adjust ")
#         cart[newEdit] = 0

#     else:
#        print("invalid input")
# else: 
#     print("Invalid number pick 1-4")



