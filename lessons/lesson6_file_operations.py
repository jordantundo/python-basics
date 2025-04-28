"""
Lesson 6: File Operations

I practiced reading and writing files in Python.
"""

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("This is my first file operation in Python!")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:", content)