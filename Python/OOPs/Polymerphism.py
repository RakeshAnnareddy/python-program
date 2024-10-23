class Cat:
    def sound(self):
        return "Meow"
    
class Dog:
    def sound(self):
        return "Boww"
    
def AnimalSounds(Animal):
    return Animal.sound()

Animals= [Cat(),Dog()]
for Animal in Animals:
    print(AnimalSounds(Animal))
    
