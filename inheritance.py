# Inheritance = Allows a class to inherit attributes and methods from another class 
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    is_Alive = True

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog1 = Dog("Scobby")
cat1 = Cat("Garfield")
mouse1 = Mouse("Mickey")

print(dog1.name)
print(dog1.is_Alive)

dog1.eat()
dog1.sleep()