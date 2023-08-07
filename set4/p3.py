# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"

def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:i]

    return prefix

# Test the function
input_list = ["flower", "flow", "flight"]
result = longest_common_prefix(input_list)
print(result)  # Output: "fl"
