

##method overloading

class OverloadDemo:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

obj = OverloadDemo()
print(obj.add(2, 3))       # Error: only the last defined method is accessible
print(obj.add(2, 3, 4))    # Output: 9




# Method Overriding:
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Usage
dog = Dog()
cat = Cat()

dog.make_sound()  # Output: Woof!
cat.make_sound()  # Output: Meow!
