# 1. Write code that asks the user for their name,
# then opens a file called name.txt and writes that name to it.
# Use open and close.
name = input("What is your name?: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. In the same file, but as if it were a separate program,
# write code that opens "name.txt" and reads the name (as above)
# then prints (note the exact output), Hi Bob! (or whatever the name is in the file).
# Do not simply print the user's input variable!
in_file = open("name.txt")
# Read and print "Hi {name}!" from file without a new line at the end
print(f"Hi {in_file.readline().strip()}!")
in_file.close()

# 3. Create a text file called numbers.txt and save it to the prac directory.
# Put the numbers 17, 42, 100 on separate lines in the file and save it.
# Write code that opens numbers.txt, reads only the first two numbers,
# adds them together then prints the result (should be 59). Use with (don't need close).

# The variable infile was used rather than in_file so that previous code does not have to be commented out
with open("numbers.txt", "r") as infile:
    line_1 = int(infile.readline())  # Read first line
    line_2 = int(infile.readline())  # Read second line
    print(line_1 + line_2)  # -> 59

# 4. Write a fourth block of code that prints the total for all lines in numbers.txt.
# This should work for a file with any numbers. Use with.
total = 0  # Set the total as 0 initially
with open("numbers.txt", "r") as infile:
    for line in infile:
        total += int(line)  # Add the integer from each line to get a total

print(total)
