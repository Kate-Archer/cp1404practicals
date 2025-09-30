"""
Prac 03
Random Numbers
"""
# line 1 with randint will produce only integers (whole number)
# line 1 will produce a random value from 5 to 20 (inclusive)
# line 2 will produce a random value ranging from 3 to 10 (excluding 10),
# increasing by 2 from 3 (3+2), therefore only odd numbers will be produced.
# line 3 is similar to the line 1 method but will not round as an integer.
# Produce a random number between 1 and 100 inclusive without rounding
import random
print(random.randint(1, 100))