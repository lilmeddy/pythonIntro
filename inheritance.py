class person:
    def __init__(self,first,last) -> None:
        self.first = first
        self.last = last
    
    def greeting(self):
        print(f"My name is {self.first} {self.last}")

class student(human)