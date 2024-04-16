class car:
    # name = "Tesla"
    def __init__(self,name,color,tyres) -> None:
        self.name = name 
        self.color = color
        self.col = tyres
    def move(self,distance):
        print(f"The {self.name} car is moving hehe at {distance}km/hr. The color is {self.color} with {self.col} numbers of tyres ")
        
var = car("Tesla","Red","4")
# print(var.name)

var.move("20")