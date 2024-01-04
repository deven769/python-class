class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def run(self):
        print("Mammal runs")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

# Creating instances of each class
animal_obj = Animal()
mammal_obj = Mammal()
dog_obj = Dog()

# Calling methods
animal_obj.speak()   # Output: Animal speaks
mammal_obj.speak()   # Output: Animal speaks
mammal_obj.run()     # Output: Mammal runs
dog_obj.speak()      # Output: Animal speaks
dog_obj.run()        # Output: Mammal runs
dog_obj.bark()       # Output: Dog barks
