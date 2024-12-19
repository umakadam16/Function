# WAP to get factorial of a number using function
def python_def_Factorial(n):
    result = 1
    for i in range(1, n + 1): 
        result *= i  
    return result
n=5
result= python_def_Factorial(5)
print("the number is ",n,"factorial is",result)

