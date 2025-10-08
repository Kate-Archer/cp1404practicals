"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly. Display subject details (subject, lecture, students)."""
    subjects = load_subjects(FILENAME)
    display_subject_details(subjects)


def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    # Open file and read data from file formatted.
    subject = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        subject.append(parts)  # Add all parts

    input_file.close()
    return subject


def display_subject_details(subjects):
    """Display subject data neatly (subject, teacher, number of students)."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")
        # print("{} is taught by {:12} and has {:3} students".format(*subject))


main()
