class MyClass:
    def __init__(self):
        self.__private_attribute = 10

    def _private_method(self):
        print("This is a private method")

obj = MyClass()
print(obj._private_method())
# Accessing private attribute and method (not recommended)
# print(obj._MyClass__private_attribute)  # Output: 10
# obj._MyClass__private_method()           # Output: This is a private method



class MyClass:
    def __init__(self):
        self._protected_attribute = 20

    def _protected_method(self):
        print("This is a protected method")

obj = MyClass()
# Accessing protected attribute and method
print(obj._protected_attribute)    # Output: 20
obj._protected_method()             # Output: This is a protected method
