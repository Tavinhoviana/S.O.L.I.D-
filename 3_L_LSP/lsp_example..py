class Animal:
    def eat(self):
        print("the animal is eating")

    def walking(self):
        print("the animal is walking")

class feline(Animal):
    def sleeping(self):
        print("the feline is sleeping")

class lion(feline):
    def roar(self):
        print("the lion is roaring")

class people:
    def speak(self, animal: Animal):
        animal.eat()        


otavio = people()
animal = Animal()
feline = feline()

animal.eat()
feline.eat()
otavio.speak(feline)