# Note break is use to stop while continue is use to skip an iteration 
# eg 

for i in range(7):
    if i == 4:
        continue
    print(i)
    print("help")
    
for i in range (20,0,-2):
    print(i)
num=[]
for i in range(1,20):
    if i%2 != 0:
        continue
    num.append(i)
print(num)