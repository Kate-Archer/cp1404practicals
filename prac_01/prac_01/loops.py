# for range 1 to 20, add by 2 (odd numbers)
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print a number of stars (integer),
# ask the user for a number,
# then print that many stars (*), in one line
number_of_stars = int(input("Number of stars *: "))
for i in range(number_of_stars):
    print('*', end=' ')
# allow a new line after every 20th *. improves visuals
    if i %20 == 0:
        print()
print()

# d. print n lines of increasing stars.
# ask the user for a number.
number_of_star_lines = int(input("Number of star lines *: "))
for i in range(1, number_of_star_lines + 1):
    print('*' * i)
print()

