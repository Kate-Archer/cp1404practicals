# Pseudocode:
#     get name
#     display menu
#     get choice
#     while choice != Q
#        if choice == H
#            display "hello" name
#        else if choice == G
#            display "goodbye" name
#        else
#            display invalid message
#        display menu
#        get choice
#     display finished message
menu_string = "(H)ello\n(G)oodbye\n(Q)uit"
name_given = str(input("Enter name:"))
print(menu_string)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello",name_given)
    elif choice == "G":
        print("Goodbye",name_given)
    else:
        print("Invalid option")
    print(menu_string) # prompts again
    choice = input(">>> ").upper()
print("Finished, thank you.") # closes loop