# 7. **Climbing Stairs**: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#     - *Input*: 3
#     - *Output*: "3"

def climb_stairs(n):
    if n == 0 or n == 1:
        return 1

    # Initialize a table to store the number of ways for each step
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 1
    dp[1] = 1

    # Calculate the number of ways for each step starting from step 2
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Test the function
n_steps = 3
result = climb_stairs(n_steps)
print(result)  # Output: 3
