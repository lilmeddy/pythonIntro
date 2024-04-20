numbers =[100,23,45,63,72,83,28,15,20,31,1,23,18,24]
sortNum =[]

# for number in range(len(numbers)):
#     if number > 0  and number < len(numbers)-1:
#         for i in range(1,numbers):
#            if numbers[number] > numbers[number +1]:
#                keep =numbers[number]


for num in numbers:
    isSorted = True
    for i in range(len(sortNum)):
      if num < sortNum[i]:
         sortNum.insert(i,num)
         isSorted= False
    if isSorted :
       sortNum.append(num)

       
print(sortNum)
       
          