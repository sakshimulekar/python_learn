# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."
import math
def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
    

if __name__ == "__main__":
    num = 9
    if(is_prime(num)):
        print(f"{num} is prime")
    else :
        print(f"{num} not prime")