# Prompt the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print asterisks in each column
    for col in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1
