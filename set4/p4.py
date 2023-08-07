# 4. **String Permutations**: Write a Python function to calculate all permutations of a given string.
#     - *Input*: "abc"
#     - *Output*: "['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"

def get_permutations(s):
    if len(s) <= 1:
        return [s]

    permutations = []

    for i in range(len(s)):
        # Swap the current character with the first character
        s_list = list(s)
        s_list[0], s_list[i] = s_list[i], s_list[0]
        new_string = ''.join(s_list)

        # Get permutations for the remaining characters (excluding the first character)
        remaining_permutations = get_permutations(new_string[1:])

        # Combine the first character with each permutation of the remaining characters
        for perm in remaining_permutations:
            permutations.append(new_string[0] + perm)

    return permutations

# Test the function
input_string = "abc"
result = get_permutations(input_string)
print(result)
