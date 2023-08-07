# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"
#first approach :
# def rev(i):
#     return "".join(reversed(i))
    
# if __name__ == "__main__":
#     input = "Python"
#     ans = rev(input)
#     print(ans)

# second approach :
# def checking(s):
#     strn = ''
#     for i in s:
#         strn = i + strn
#     return strn


# if __name__ == "__main__":
#     str = "Hello, world!"
#     reversed_str=checking(str)
#     print(reversed_str)

#third approach
def checking(s):
    return s[::-1]


if __name__ == "__main__":
    str = "Hello, world!"
    reversed_str=checking(str)
    print(reversed_str)