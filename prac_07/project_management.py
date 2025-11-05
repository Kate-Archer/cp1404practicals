"""
Project management
Prac 07
time estimate: 2 hour
5+ hours
"""
from prac_07.project import Project
DEFAULT_FILENAME = "projects.txt"
import csv


def load_projects():
    """Load projects from a valid filename entered by the user (or use default)."""
    from datetime import datetime
    projects = []
    while True:
        filename = input(f"Provide a filename to load projects from (enter for default: {DEFAULT_FILENAME}): ").strip()
        # Use default file if enter is pressed
        if filename == "":
            filename = DEFAULT_FILENAME
        # Allow user to cancel with a space
        if filename.isspace():
            print("Cancelled loading projects.")
            return None, []
        try:
            with open(filename, "r", encoding="utf-8") as in_file:
                in_file.readline()  # Skip header
                for line in in_file:
                    parts = line.rstrip("\n").split("\t")
                    if len(parts) < 5:
                        continue  # Skip invalid lines
                    name = parts[0]
                    start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
                    priority = int(parts[2])
                    cost_estimate = float(parts[3])
                    completion_percent = int(parts[4])
                    project = Project(name, start_date, priority, cost_estimate, completion_percent)
                    projects.append(project)
            print(f"Loaded {len(projects)} project(s) from '{filename}'.")
            return filename, projects
        except FileNotFoundError:
            print(f"The file '{filename}' was not found. Try again or press space to cancel.")



def main():
    """Main"""
    project, projects = load_projects()

    menu = "Menu:\nL - Load projects\nS - Save projects\nD - Display projects\nF - Filter projects by date\nA - Add new project\nU - Update  project\nQ - Quit"
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename, projects = load_projects()

        elif choice == "S":
            filename = save_project(projects)

        elif choice == "D":
            max_length_name, max_length_date, max_length_priority, max_length_cost, max_length_completion = compute_max_lengths(projects)
            # Separate projects by completion status
            display_projects(max_length_completion, max_length_cost, max_length_date, max_length_name,
                             max_length_priority, projects)

        elif choice == "F":
            from datetime import datetime

            given_date = input("Show projects that start after date (dd/mm/yyyy): ").strip()
            try:
                filter_date = datetime.strptime(given_date, "%d/%m/%Y").date()
            except ValueError:
                print("Invalid date format. Please use dd/mm/yyyy.")
                continue

            # Filter and sort
            filtered_projects = [project for project in projects if project.start_date > filter_date]
            filtered_projects.sort() # Sort dates via  __lt__

            if filtered_projects:
                print(f"\nProjects starting after {filter_date.strftime('%d/%m/%Y')}:")
                for p in filtered_projects:
                    print(f"  {p}")
            else:
                print(f"No projects start after {filter_date.strftime('%d/%m/%Y')}.")


        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(menu)
        # Convert lowercase menu input to uppercase
        choice = input(">>> ").upper()

    final_choice = input(">>> Do you want to save projects.txt (default file)? (Y/N):").upper()
    if final_choice == "Y":
        # save file
        pass


def display_projects(max_length_completion: int, max_length_cost: int, max_length_date: int, max_length_name: int, max_length_priority: int, projects):
    """Display projects grouped by completion status and sorted by highest priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    # Sort each list by highest priority (__lt__)
    incomplete_projects.sort()
    complete_projects.sort()

    # Display both groups
    print("\nIncomplete projects:")
    for project in incomplete_projects:
        print(
            f"{project.name:<{max_length_name}}  {project.start_date:<{max_length_date}}  {project.priority:<{max_length_priority}}  {project.cost_estimate:<{max_length_cost}.2f}  {project.completion_percent:<{max_length_completion}}%")

    print("\nComplete projects:")
    for project in complete_projects:
        print(
            f"{project.name:<{max_length_name}}  {project.start_date:<{max_length_date}}  {project.priority:<{max_length_priority}}  {project.cost_estimate:<{max_length_cost}.2f}  {project.completion_percent:<{max_length_completion}}%")


def save_project(projects):
    """Prompt user for a valid filename to save projects to (default file if none specified)."""
    while True:
        filename = input(f"Provide a filename to save projects to (default: {DEFAULT_FILENAME}): ").strip()
        # Use default file if enter is pressed
        if filename == "":
            filename = DEFAULT_FILENAME
        # Allow user to cancel with a space
        if filename.isspace():
            print("Cancelled saving projects.")
            return None
        try:
            with open(filename, "w", encoding="utf-8", newline="") as out_file:
                out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
                for project in projects:
                    out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percent}\n")

            print(f"Projects successfully saved to '{filename}'.")
            return filename

        except FileNotFoundError:
            print(f"The file '{filename}' was not found. Try again or press Space to cancel.")

def compute_max_lengths(projects):
    """Compute the maximum length for project name, start date, priority, cost estimate and completion percentage."""
    max_length_name = max(len(project.name) for project in projects)
    max_length_date = max(len(str(project.start_date)) for project in projects)
    max_length_priority = max(len(str(project.priority)) for project in projects)
    max_length_cost = max(len(f"{project.cost_estimate:.2f}") for project in projects)
    max_length_completion = max(len(f"{project.completion_percent}%") for project in projects)

    return max_length_name, max_length_date, max_length_priority, max_length_cost, max_length_completion


main()



