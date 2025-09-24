"""
CP1404
create text file temp_input with 15 value floats (-200 to 200) (random)
get the numbers from a python function
convert temps, read the values in as Fahrenheit
read the values out as Celsius
"""
import random


def main():
    """Convert input file of a random temperature unit to the output file of another unit."""
    create_input_file(15)
    input_fahrenheit_file = open("temps_fahrenheit_input.txt", "r")
    output_celsius_file = open("temps_celsius_output.txt", "w")

    for line in input_fahrenheit_file:
        """Read lines in file."""
        # Read each line from the file input_fahrenheit_file one at a time, in a loop.
        result = convert_fahrenheit_to_celsius(float(line.strip().replace("F", "")))
        # Removes the F character so python works with a float and not a string
        print(f"{result:.2f}C", file=output_celsius_file)

    input_fahrenheit_file.close()
    output_celsius_file.close()


def create_input_file(quantity):
    """Write number (quantity) of temperatures to file. This starts with a temperature in Fahrenheit."""
    temperatures_file = open("temps_fahrenheit_input.txt", "w")
    for i in range(quantity):
        temperature = random.uniform(-200, 200)
        print(f"{temperature:.2f}F", file=temperatures_file)

    temperatures_file.close()


def convert_celsius_to_fahrenheit(celsius):
    """Convert given Celsius value to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert given Fahrenheit value to Celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
