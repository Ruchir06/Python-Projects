# multiple inheritance -    inherit from more than parent class 
#                           eg. Class Honda(Car, Bike)
# multilevel inheritance -  inherit from a parent which inherits from another parent
#                           eg. C(A) <- B(A) <- A

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey): 
    pass

class Hawk(Predator):
    pass 

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("hawk1")
fish = Fish("Nemo")


hawk.hunt()
fish.hunt()

fish.sleep()