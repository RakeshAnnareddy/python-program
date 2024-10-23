class Animal:
    def __init__(self,name,age):
        self.name= name
        self.age= age
        
    def info(self):
        return f"{self.name}"
    
class AnimalName(Animal):
    def info(self):
        return f"It is {self.name} and its age is {self.age}"
    
panda= AnimalName("Panda",'20')

print(panda.info())
