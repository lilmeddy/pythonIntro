class person:
    def __init__(self,first,last) -> None:
        self.first = first
        self.last = last
    
    def greeting(self):
        print(f"My name is {self.first} {self.last}")
class student(person):
    pass 
class studentchild(student):
    pass
# var = student("mede","ede")
var = studentchild("mede","ede")
var.greeting()