### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

# ```
# str1 = PyNaTive
# ```

# **Expected Output**:
str1 = "PyNaTive"

# Define a custom sorting function
def custom_sort(char):
    return char.isupper(), char

# Sort the characters of the string using the custom sorting function
sorted_str1 = ''.join(sorted(str1, key=custom_sort))

print(sorted_str1)
