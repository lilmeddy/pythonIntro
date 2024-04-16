class car:
    # name = "Tesla"
    def __init__(self,name,color,tyres) -> None:
        self.name = name 
        self.color = color
        self.col = tyres
        self.speed = 0
    def move(self,distance):
        self.speed = distance
        print(f"The {self.name} car is moving hehe at {distance}km/hr. The color is {self.color} with {self.col} numbers of tyres ")
    def greeting(self,greet):
        print(f"The {self.name} driver {greet} is speeding at {self.speed}km/hr ")
var = car("Tesla","Red","4")
# print(var.name)
var.move("20")
var.greeting("Osamede")
