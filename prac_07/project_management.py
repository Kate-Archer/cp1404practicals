"""
Project management
Prac 07
time estimate: 1 hour
start 8:33
"""

def load_projects():
    with open("projects.txt", "r") as in_file:
        pass


def main():
    """Main"""
    print("Menu:\nL - Load projects\nS - Save projects\nD - Display projects\nF - Filter projects by date\nA - Add new project\nU - Update  project\nQ - Quit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
    final_choice = input(">>> Do you want to save projects.txt (default file)? (Y/N):").upper()
    if final_choice == "Y":
        # save file
        pass
    else:
        pass







main()



