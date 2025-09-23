# create a program allowing students to learn number sequences

# create a program allowing students to learn number sequences


menu = "Menu:\n1. Show even numbers from X to Y\n2. Show odd numbers from X to Y\n3. Show the squares from X to Y\n4. Exit the program"

print(menu)

x = int(input("Please enter X: "))
y = int(input("Please enter Y: "))

choice = input(">>> ")

while choice != "4":
    if choice == "1":
        for i in range(x, y + 1):
            if i % 2 == 0: # even
                print(i, end=' ')
        print()  # adds a newline after all numbers are printed
    elif choice == "2":
        for i in range(x, y + 1):
            if i % 2 != 0: # odd, not divisible by 2, it has a remainder, not 0
                print(i, end=' ')
        print()
    elif choice == "3":
        for i in range(x, y + 1):
            print(i ** 2, end=' ') # power
        print()
    else:
        print("Invalid option")

    print(menu)
    choice = input(">>> ")

print("Finished, thank you.")
