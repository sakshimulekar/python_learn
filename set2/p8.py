### Problem **8: Initialize dictionary with default values**

# In Python, we can initialize the keys with the same values.

# **Given**:

# ```
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# ```

# **Expected output:**

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Initialize the dictionary with default values for each employee
employee_info = {employee: defaults for employee in employees}

print(employee_info)
