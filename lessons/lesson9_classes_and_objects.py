"""
Lesson 9: Classes and Objects

Understanding classes and objects made me appreciate OOP in Python.
"""

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())