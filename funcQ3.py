# Write a program to check whether a person can vote or not using a function:
def can_vote(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

age = int(input("Enter your age"))
result = can_vote(age)
print (result)
