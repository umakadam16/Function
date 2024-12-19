#WAP to find maximum among two number
def find_maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

maximum = find_maximum(num1, num2)
print(f"The maximum of {num1} and {num2} is {maximum}.")
