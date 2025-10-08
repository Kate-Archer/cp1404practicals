"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
from typing import Any


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months?: "))

    for month in range(1, number_of_months + 1):
        # income = float(input("Enter income for month " + str(month) + ": "))
        income = float(input(f"Enter income for month {month} :"))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """ Print the report with incomes and number of months present. """
    # Print the income report, starting with a total of 0 and accumulating per month and income input
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
