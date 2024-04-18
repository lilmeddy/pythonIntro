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
        self.name = input("Enter fullname ")
        age = input("Enter your age ")
        self.user.append([self.name,age])
class firstbank(auth):
    def __init__(self, bank) -> None:
        super().__init__(bank) #makes the firstbank have all the attributes of auth so it's important if you want the attribute
        auth.__init__(bank) #another way to do it instead of super 
        print(f"Welcome to {bank}")
        self.register()
        phone = input("Enter phone number +234 ")
        for i in self.user:
            if i[0] == self.name:
                i.append(phone)
        print(self.user)
firstbank("firstbank")
    
nam = ("mede","tayo","timi")
name = iter(nam)
print(next(name))
print(next(name))
print(next(name))

