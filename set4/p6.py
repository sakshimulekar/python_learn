# 6. **Missing Number**: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#     - *Input*: [3, 0, 1]
#     - *Output*: "2"

def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    return missing_number

# Test the function
input_nums = [3, 0, 1]
result = find_missing_number(input_nums)
print(result)  # Output: 2
