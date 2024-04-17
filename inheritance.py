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

class auth:
    def __init__(self,bank) -> None:
        self.bank = bank
        self.user =[]
    def register(self):
        name = input("Enter fullname ")
        age = input("Enter your age ")
        self.user.append([name,age])
class firstbank(auth):
    def __init__(self, bank) -> None:
        super().__init__(bank) #makes the firstbank have all the attributes of auth so it's important if you want the attribute
        print(f"Welcome to {bank}")
        self.register()
        print(self.user)
firstbank("firstbank")
      