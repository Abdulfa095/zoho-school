def print_pattern(letter):
    # Get the ASCII value of the letter
    n = ord(letter) - ord('A') + 1  # This will give the number of rows/columns

    # Loop to print each row of the pattern
    for i in range(n):
        for j in range(n):
            # Print the letter at the borders of the pattern
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print(letter, end=" ")
            else:
                print(" ", end=" ")
        print()
letter = input("Enter an alphabet (A-Z): ").upper()
if 'A' <= letter <= 'Z':
    print_pattern(letter)
else:
    print("Please enter a valid alphabet between A and Z.")
