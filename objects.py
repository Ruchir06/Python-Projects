# Object -    A bundle of related attributes (Variables) and methods (Functions) 
#             You need a class to create objects

# class -    BluePrint used to design the structures and layouts of an object

class Car:
    def __init__(self, model, year, color, is_For_Sale):
        self.model = model
        self.year = year
        self.color = color
        self.is_For_Sale = is_For_Sale
    
    def __str__(self):
        return f"model: {self.model}, year: {self.year}, color: {self.color}, is_For_Sale: {self.is_For_Sale}"

    def start(self):
        print(f"You drive the {self.model}")
    
    def stop(self):
        print(f"Stop the {self.model}")

car1 = Car("Toyota", 2024, "Red", False)
car2 = Car("Ford", 2025, "Blue", True)
print(car1)


car1.start()
car2.stop()