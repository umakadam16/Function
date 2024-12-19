def print_table(number):
    print(f"Table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


num = int(input("Enter a number to get its table: "))

print_table(num)
