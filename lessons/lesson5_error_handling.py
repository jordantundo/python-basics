"""
Lesson 5: Error Handling

In this lesson, I discovered how to handle errors gracefully.
"""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! Cannot divide by zero.")