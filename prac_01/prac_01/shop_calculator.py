# shop requires a small program that allows them to work out the
# total price for a number of items, with differing prices.
total_price = 0 # starts at 0
number_of_items = int(input("The number of items: "))
while number_of_items < 0:
    print("Invalid number of items! Try again.")
    number_of_items = int(input("The number of items: "))
for i in range(number_of_items):
    item_price = float(input("The item price:$ "))
    total_price += item_price # increases per item
print(f"The total price for {number_of_items} items is:${total_price:.2f}")
if total_price > 100:
    discount_price = total_price * 0.9
    print(f"The discount price is:${discount_price:.2f}")
else:
    print("There is no discount")