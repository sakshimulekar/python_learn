# 10. **Contains Duplicate**: Given an array of integers, find if the array contains any duplicates.
#     - *Input*: [1, 2, 3, 1]
#     - *Output*: "True"

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

# Test the function
input_array = [1, 2, 3, 1]
result = contains_duplicate(input_array)
print(result)  # Output: True
