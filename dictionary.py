# create a dictionary for a car
car={
    "brand":"corolla",
    "tyres":8,
    "color":"carton color",
    "gear":"automatic",
    "carSeat":"5"
}
# print(car)
# car["brand"]="tesla"
# print(car)

# combining dictionaries 
car.update({"hobbies":{"favorite":"hockey",
                       "others":["football", "basketball"]}})
print(car["hobbies"]["others"][1])
# or 
hobbies = car["hobbies"]
others = hobbies["others"]
football = others[0]
print(football)
print(car.keys())
print(list(car.keys())[1])

# \n to break line he finally said it lol 
