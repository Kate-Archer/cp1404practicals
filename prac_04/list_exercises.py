"""
CP1404/CP5632 Practical
List exercises
"""

# 1. Numbers
numbers = []
for i in range(5):
    number = int(input("Give a number please (5 total): "))
    numbers.append(number)
print(f"The first number is {numbers[0]}!")
print(f"The last number is {numbers[-1]}!")
print(f"The smallest number is {min(numbers)}!")
print(f"The largest number is {max(numbers)}!")
print(f"The average of the numbers is {(sum(numbers) / len(numbers))}!")

# 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("What is your username?: ")
# Reprompt the user for a username until a valid username is input.
while username not in usernames:
    print("Access denied")
    username = input("What is your username?: ")
print("Access granted")
