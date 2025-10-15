"""
CP1404/CP5632 Practical
Hexadecimal colour lookup
"""

# Add dictionary of colour to code values
COLOUR_TO_CODE = {"amethyst": "#9966cc", "aqua": "#00ffff",
                  "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
                  "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
                  "aquamarine1": "#7fffd4", "bittersweet": "#fe6f5e",
                  "aquamarine4": "#458b74", "azure1": "#f0ffff",
                  "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                  "baby pink": "#f4c2c2", "bleu de france": "318ce7"}

# Print the colour and relating code nicely
max_length_colour = max(len(colour) for colour in COLOUR_TO_CODE)
max_length_code = max(len(code) for code in COLOUR_TO_CODE)
for colour, code in COLOUR_TO_CODE.items():
    print(f"{colour:<{max_length_colour}} is {code:>{max_length_code}}")

# Print the correlating code based on a valid colour input in
colour_name = input("Please enter a colour name: ").lower()
while colour_name != "":
    # print(f"The code for \"{colour_name}\" is {COLOUR_TO_CODE.get(colour_name)}")
    # colour_name = input("Enter a colour name: ").lower()
    # or
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")

    colour_name = input("Please enter a colour name: ").lower()
