# ask user for low
# ask user for high number
# ensure high is > low
# print n * :) where
# n is random number between low and high
# import random
#
# low = int(input("Give a low number:"))
# high = int(input("Give a high number:"))
# if low < high: # good, but will only run once!
#     n = random.randint(low, high)
#     print(n * ":)")
# else:
#     print("Invalid. Low < high only.")  # good description.
#     low = int(input("Give a low number:")) # repeat line not necessary, just need to update high
#     high = int(input("Give a high number:"))
#     n = random.randint(low, high) # too simple, what is n?
#     print(n*":)")


# teacher way
from random import randint

low = int(input("Low: "))
high = int(input("High: "))
while low >= high: # while input is bad only. good because while can run as many times as wanted.
    print("error")
    high = int(input("High: ")) # only high repeated, good
    print(":)"* randint(low, high))
# or can do number_of_smiles for randint(low, high)

# i will now "input_number" for example of a function
# boeleans are exception

# math is a module
# math, pi is a name existing in the module (math.pi) name defined inside . or child
# input().upper() right (child, member, string) of left (input, module). upper is a member of string

# brothers wives is a syntax error, grammar, multiple meanings, ' missing


