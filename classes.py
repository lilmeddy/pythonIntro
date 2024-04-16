class car:
    # name = "Tesla"
    def __init__(self) -> None:
        self.name = "Tesla"  
    def move(self):
        print(f"The {self.name} is moving hehe")
var = car()
# print(var.name)
var.move()