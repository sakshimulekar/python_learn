# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Test the function
numerator = 5
denominator = 0
result = divide_numbers(numerator, denominator)
print(result)  # Output: "Cannot divide by zero."
