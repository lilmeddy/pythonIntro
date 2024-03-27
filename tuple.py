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