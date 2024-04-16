class car:
    # name = "Tesla"
    def __init__(self) -> None:
        self.name = "Tesla"  
    def move(self,distance):
        print(f"The {self.name} car is moving hehe as move {distance}km/hr")
        
var = car()
# print(var.name)
var.move(distance=10)