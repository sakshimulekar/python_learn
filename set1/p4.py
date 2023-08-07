# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"

def average(input):
    total = sum(input)
    l = len(input)
    ans = total / l
    return ans
    
        


if __name__ == "__main__":
    list=[10,20,30,40]
    res = average(list)
    print(res)
    