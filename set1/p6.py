# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

def checkVow(input):
    vow = "aeiou"
    c = 0
    for char in input:
        if char in vow:
            c += 1
    return c

if __name__ == "__main__":
    input = "hello"
    c = checkVow(input)
    print(c)