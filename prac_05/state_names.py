"""
CP1404 Practical
State names in a dictionary
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
# Print the states and names neatly with string formatting
max_length_name = max(len(name) for name in CODE_TO_NAME)
max_length_code = max(len(code) for code in CODE_TO_NAME)
for code, name in CODE_TO_NAME.items():
    print(f"{code:<{max_length_code}} is {name:>{max_length_name}}")
# Print the name based on a valid state code
state_code = input("Please enter a short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
