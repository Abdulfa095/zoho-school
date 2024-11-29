def generate_tables(number):
    print(f"Multiplication Table for {number}:\n")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
    print(f"\nSubtraction Table for {number}:\n")
    for i in range(1, 11):
        print(f"{number} - {i} = {number - i}")
num = int(input("Enter a number: "))
generate_tables(num)
