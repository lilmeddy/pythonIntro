class car:
    # name = "Tesla"
    def __init__(self,name,color,tyres) -> None:
        self.name = name 
        self.color = color
        self.col = tyres
        self.speed = 0
        self.move("20")
        self.greeting("Osamede")
    def move(self,distance):
        self.speed = distance
        print(f"The {self.name} car is moving hehe at {distance}km/hr. The color is {self.color} with {self.col} numbers of tyres ")
    def greeting(self,greet):
        print(f"The {self.name} driver {greet} is speeding at {self.speed}km/hr ")
var = car("Tesla","Red","4")
# print(var.name)


class dog:
    def __init__(self,name,color,breed) -> None:
        self.name = name 
        self.color = color
        self.breed = breed
        self.bark("woahhhhhhh")
    def bark(self,bark):
        print(f"Osamede's dog '{self.name} a {self.color} {self.breed} ' is barking {bark}")
var = dog("Roxy","White","Eskimo")

        
# assigment a class authentication then next register and login 
