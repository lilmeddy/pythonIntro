# name = input("whats your name: ")
# name2 = input("whats your name: ")
# age = input("whats my age: ")
# age2 = input("whats my age: ")
# if (name ==name2) and (age==age2):
#     print("you passed")
# elif (name==name2):
#     print("You passsed halfway")
# else:
#     print("you failed")


mede = int(input("Enter your score mede: "))
duro = int(input("Enter your score duro: "))
obafemi = int(input("Enter your score obafemi: "))
ibrahim = int(input("Enter your score ibrahim: "))
timi = int(input("Enter your score timi: "))
totalScore = mede + duro + obafemi + ibrahim + timi
meanScore = int(totalScore/5)
if (meanScore >= 70):
    print(f"The total score is {meanScore}. They all Passed cute hehe")
else:
    print(f"The total score is {meanScore}. They all failed sad lol")