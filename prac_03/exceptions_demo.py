"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


# 1) A ValueError will occur when an invalid non-integer is input as the numerator or denominator.
# 2) A ZeroDivisionError will occur when the denominator is input as a zero, as the numerator cannot be divided by zero.
# 3) To avoid the ZeroDivisionError, the code below can be used:
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
while denominator == 0 :
    print("Cannot divide by zero!")
    denominator = int(input("Enter the denominator: "))
fraction = numerator / denominator
print(fraction)