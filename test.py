name = input(" ")
tag = False
while tag == False:
    new = name.split(" ")
    for i in new:
        if i != "":
            tag = i
    if tag == False:
        print("Error")
        name = input("")
print(tag)