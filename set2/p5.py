### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# **Given**:

# ```
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# ```

# **Expected output:**

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Determine the length of the new list (the longer of the two lists)
max_len = max(len(list1), len(list2))

# Create a new list by concatenating items index-wise
concatenated_list = [list1[i] + list2[i] for i in range(max_len)]

print(concatenated_list)
