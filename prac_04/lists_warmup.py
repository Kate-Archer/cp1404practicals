"""
CP1404/CP5632 Practical
Lists "warm-up"
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1] # from 3, excluding the 4th one
# 5 in numbers = numbers[4] or True
# 7 in numbers = False
# "3" in numbers = False (3, not "3")
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Python expressions
numbers[0] = "ten"
numbers[-1] = 1
numbers[2:] = [4, 1, 5, 9, 2] # All but the first 2

print(9 in numbers)
# or to be more specific
if 9 in numbers:
    print("9 is an element of numbers")
