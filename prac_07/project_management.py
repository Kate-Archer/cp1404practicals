"""
Project management
Prac 07
time estimate: 2 hour
8~ hours
"""
from prac_07.project import Project
from datetime import datetime
import datetime as dt

DEFAULT_FILENAME = "projects.txt"


def load_projects():
    """Load projects from a valid filename entered by the user (or use default)."""
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
    """
    Program menu
    L - Load projects (Prompt for a filename and load projects (dates as dd/mm/yyyy)).
    S - Save projects (Prompt for a filename and save the current projects.
    D - Display projects (Incomplete and Complete (sorted by priority, 1 = highest)).
    F - Filter projects by date (Ask for a date (dd/mm/yyyy) and list projects (sorted) starting after that date.
    A - Add new project and save (Inputs: name, start date (dd/mm/yyyy), priority (>=1), cost (>0), completion % (0–100)).
    U - Update project (Choose a project, then optionally change priority and/or completion % (press Enter to keep current)).
    Q - Quit (Exit the program, optionally save project if prompted with "Y").
    """
    # Load the projects from the selected file
    project, projects = load_projects()

    menu = "Menu:\nL - Load projects\nS - Save projects\nD - Display projects\nF - Filter projects by date\nA - Add new project\nU - Update  project\nQ - Quit"
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename, projects = load_projects()

        elif choice == "S":
            # Save project
            filename = save_project(projects)

        elif choice == "D":
            # Compute max lengths of attributes (values)
            max_length_name, max_length_date, max_length_priority, max_length_cost, max_length_completion = compute_max_lengths(
                projects)
            # Separate projects by completion status
            display_projects(max_length_completion, max_length_cost, max_length_name,
                             max_length_priority, projects)

        elif choice == "F":
            max_length_name, max_length_date, max_length_priority, max_length_cost, max_length_completion = compute_max_lengths(
                projects)
            # Filter projects based on date
            filter_project_dates(max_length_completion, max_length_cost, max_length_date, max_length_name,
                                 max_length_priority, projects)

        elif choice == "A":
            # Add a valid project to the chosen file and Project class (name, start date, priority, cost estimate, completion percentage)
            name = str(input("Project name (enter to cancel):")).title()
            while name != "":
                start_date = get_valid_date()
                priority = get_valid_priority()
                cost_estimate = get_valid_cost()
                completion_percent = get_valid_percent()
                project = Project(name, start_date, priority, cost_estimate, completion_percent)
                projects.append(project)
                save_project(projects)
                # Display added project
                # Shortcut: do this instead
                print(f"{project} add.")
               # print(
               #     f"Project name:{name}, Started:{start_date}, Priority:{priority}, Cost estimate:{cost_estimate}, Completion (%):{completion_percent} added.")
               # name = str(input("Name:"))

        elif choice == "U":
            max_length_name, max_length_date, max_length_priority, max_length_cost, max_length_completion = compute_max_lengths(
                projects)
            # Select a valid project to modify
            # Update the selected project's priority or completion attribute
            update_project(max_length_completion, max_length_cost, max_length_name, max_length_priority, projects)

        else:
            print("Invalid menu choice")
        print(menu)
        # Convert lowercase menu input to uppercase
        choice = input(">>> ").upper()

    final_choice = input(">>> Do you want to save projects.txt (default file)? (Y/N):").strip().upper()
    if final_choice == "Y":
        # Save project if prompted (after quitting menu)
        filename = save_project(projects)


def display_projects(max_length_completion: int, max_length_cost: int, max_length_name: int,
                     max_length_priority: int, projects):
    """Display projects grouped by completion status and sorted by highest priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    # Sort each list by highest priority (__lt__)
    incomplete_projects.sort()
    complete_projects.sort()

    # Display both groups
    print("\nIncomplete projects:")
    for project in incomplete_projects:
        date_str = project.start_date.strftime("%d/%m/%Y")
        print(
            f"{project.name:<{max_length_name}}  {date_str}  {project.priority:<{max_length_priority}}  {project.cost_estimate:<{max_length_cost}.2f}  {project.completion_percent:<{max_length_completion}}%")

    print("\nComplete projects:")
    for project in complete_projects:
        date_str = project.start_date.strftime("%d/%m/%Y")
        print(
            f"{project.name:<{max_length_name}}  {date_str}  {project.priority:<{max_length_priority}}  {project.cost_estimate:<{max_length_cost}.2f}  {project.completion_percent:<{max_length_completion}}%")


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
                    date_str = project.start_date.strftime("%d/%m/%Y")  # Format to dd/mm/yyyy
                    out_file.write(
                        f"{project.name}\t{date_str}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percent}\n")

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


def filter_project_dates(max_length_completion: int, max_length_cost: int, max_length_date: int, max_length_name: int,
                         max_length_priority: int, projects):
    """Ask for a valid date (dd/mm/yyyy) and filter projects starting after it (sorted by date)."""
    # Keep asking until a valid date is given or the user cancels
    while True:
        given_date = input("Show projects that start after date (dd/mm/yyyy)(enter to cancel): ").strip()
        if given_date == "":  # Allow user to cancel with enter.
            print("Cancelled.")
            return
        try:
            filter_date = datetime.strptime(given_date, "%d/%m/%Y").date()
            break  # Break if a valid date is given
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")

    # Filter and sort
    filtered = [project for project in projects if project.start_date > filter_date]
    filtered.sort()

    if filtered:
        print(f"\nProjects starting after {filter_date:%d/%m/%Y}:")
        for project in filtered:
            date_str = project.start_date.strftime("%d/%m/%Y")
            print(
                f"{project.name:<{max_length_name}}  {date_str:<{max_length_date}}  {project.priority:<{max_length_priority}}  {project.cost_estimate:<{max_length_cost}.2f}  {project.completion_percent:<{max_length_completion}}%")
    else:
        print(f"No projects start after {filter_date:%d/%m/%Y}.")


def get_valid_date():
    """Prompt for a date as dd/mm/yyyy and return a valid date format."""
    while True:
        try:
            start_date = input("Enter start date (dd/mm/yyyy): ").strip()
            # Convert start date to the proper date format
            start_date = dt.datetime.strptime(start_date, "%d/%m/%Y").date()
            return start_date
        except ValueError:
            print("Date format must be dd/mm/yyyy")


def get_valid_priority():
    """Handle priority exceptions (non integer input)."""
    while True:
        try:
            priority = int(input("Priority: "))
            if priority < 1:
                # Ensure priority is 1 or more.
                print("Priority must be 1 or above.")
                priority = int(input("Priority: "))
            return priority
        except ValueError:
            print("Priority must be an integer (e.g. 1).")


def get_valid_cost():
    """Handle cost exceptions (non float or non integer input)."""
    while True:
        try:
            cost_estimate = float(input("Cost: $"))
            if cost_estimate < 0:
                print("Cost must be >=0")
                cost_estimate = float(input("Cost: $"))
            return cost_estimate
        except ValueError:
            print("Cost must be a number.")


def get_valid_percent():
    """Handle percent exceptions (non integer input)."""
    while True:
        try:
            completion_percent = int(input("Percent completed (%): "))
            # Handle percentages outside valid range
            if completion_percent < 0 or completion_percent > 100:
                print("Completion percentage is 0-100% only (whole numbers).")
                completion_percent = int(input("Percent completed (%): "))
            return completion_percent
        except ValueError:
            print("Completion percentage must be a valid number.")


def select_project(max_length_completion: int, max_length_cost: int, max_length_name: int, max_length_priority: int,
                   projects):
    """Prompt the user to select a valid project number and return the chosen project index, or None if cancelled."""
    if not projects:
        print("No projects to update.")
        return None  # Return None if project list is empty
    print("Projects:")
    for index, project in enumerate(projects, start=1):
        date_str = project.start_date.strftime("%d/%m/%Y")
        # Display the projects
        print(
            f"{index}. Name: {project.name:<{max_length_name}} | Start: {date_str} | Priority {project.priority:<{max_length_priority}} | {project.cost_estimate:<{max_length_cost}} | Completion percentage: {project.completion_percent:<{max_length_completion}}%")
    while True:
        chosen_project = input("\nEnter project number to update (Enter to cancel): ").strip()
        if chosen_project == "":
            print("Cancelled input.")
            return None
        if not chosen_project.isdigit():
            # Handle invalid non-integer input
            print(f"Please enter a number between 1 and {len(projects)}.")
            continue

        if int(chosen_project) in range(1, len(projects) + 1):
            return int(chosen_project) - 1  # Return valid project
        else:
            print(f"Please enter a number between 1 and {len(projects)}.")


def get_int_or_current(prompt, current, min_value=None, max_value=None):
    """Update a project's priority and/or completion (%), enter keeps current values."""
    while True:
        # Prompt represents priority or completion
        # Current represents the current value of the prompt (originally)
        value_chosen = input(f"{prompt} (current: {current}, Enter to keep): ").strip()
        if value_chosen == "":  # Allow current value to remain existing
            return current
        try:
            value = int(value_chosen)
            if min_value is not None and value < min_value:
                print(f"Value must be >= {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be <= {max_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a whole number or press Enter to keep the current value.")


def update_project(max_length_completion, max_length_cost, max_length_name, max_length_priority, projects):
    """
    Choose a valid project, then optionally update completion (%) and/or priority.
    Blank input keeps the existing (original) values.
    """
    selected_project = select_project(max_length_completion, max_length_cost, max_length_name,
                                      max_length_priority, projects)
    if selected_project is None:
        return  # Cancel if no projects

    project = projects[selected_project]
    print(f"\nUpdating: {project.name}")

    # Ask for new values (or keep) for priority and completion %
    new_priority = get_int_or_current("New priority", project.priority, min_value=1)
    new_complete = get_int_or_current("New completion (%)", project.completion_percent, min_value=0, max_value=100)

    # Update new values to the project list
    project.priority = new_priority
    project.completion_percent = new_complete

    print(
        f"Updated>>> Project name: {project.name:<{max_length_name}} | Priority: {project.priority:<{max_length_priority}} | Completion percentage: {project.completion_percent:<{max_length_completion}}%")

    # Give the option to save immediately
    save_now = input("Save changes to file now? (Y/N): ").strip().upper()
    if save_now == "Y":
        save_project(projects)


main()
