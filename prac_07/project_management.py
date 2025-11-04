"""
Project management
Prac 07
time estimate: 1 hour
start 8:33
"""
from prac_07.project import Project


def load_projects():
    """--"""
    with open("projects.txt", "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.rstrip("\n").split("\t")
            # Construct project object using the elements
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percent = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percent)
    return project




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



