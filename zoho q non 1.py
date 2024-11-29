def generate_tables(number):
    # Multiplication Table
    print(f"Multiplication Table for {number}:\n")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
    
    # Subtraction Table
    print(f"\nSubtraction Table for {number}:\n")
    for i in range(1, 11):
        print(f"{number} - {i} = {number - i}")

# Input the number
num = int(input("Enter a number: "))
generate_tables(num)
