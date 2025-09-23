# gross_pay = float(input("What is the gross pay?:"))
# tax_rate = float(input("What is the tax rate? (use decimals):"))
# tax_amount = gross_pay*tax_rate
# net_pay = gross_pay - tax_amount
# print("The net pay is", net_pay)


# length = int(input("What is the length (m)?:"))
# import random
# width = random.randint(1, length)
# area = length * width
# print(f"The width is {width}m and area is {area}m^2")
# nums1 = [1, -5, 2, 0, 4, 2, -3]
# nums2 = [1, -5, 2, 4, 4, 2, 7]
# result = 0
# j = 0
# while j < len(nums1):
#     if nums1[j] != nums2[j]:
#         result = result + 1
#     j = j + 1
#
# print(result)
#
# x = 5
# for i in range(x):
#     x = x + i
#     print(x, end=" ")
# range(start, stop, step) so 1-9 adding 4 each time,i =  1, 5, 9
# for i in range(1, 10, 4):
#     print(i, i*2, end=" ")

# 1, 1*2, 5, 5*2, 9, 9*2

# girls = 0
# boys = 0
# children = girls + boys
# girls = 15
# boys = 12
# print(girls, boys, children)
#
# x = 10
# while x <= 10:
#     x = x - 1
#     print(x)
# numbers = [1, 2, -4, 6, -3, -9]
# result = 0
# for j in range(0, len(numbers)):
#     if numbers[j] < 0:
#         result = result + 1
# print(result)

# x = (5 / 2)
# print(x)
# division, always rounds down, so 2.5 -> 2
# x = 10
# while x > 4:
#     print(x, end=" ")
#     x = x - 2

# 10, 8, 6

# a = 5
# b = 10
# c = 0.5
# a == b * c or c * 10 >= a
# x = 1
# y = 2
# z = 3
# if x < y:
#     if y > 4:
#         z = 5
#     else:
#         z = 6
# print(z)
#
# x = 5
# y = 10
# if x < 10:
#     if y > 10 and x > 5:
#         print("A")
#     else:
#         print("B")

a = 2
b = 1
c = 3

if a > b:
    if b > c:
        answer = c
    else:
        answer = b
elif a > c:
    answer = c
else:
    answer = a

print(answer)