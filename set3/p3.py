# **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"


def two_sum(nums, target):
    # Create a dictionary to store elements and their indices
    num_index_map = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in num_index_map:
            return [num_index_map[complement], i]

        # If the complement doesn't exist, store the current element and its index in the dictionary
        num_index_map[num] = i

    # If no solution is found, return an empty list
    return []

# Test the function
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
