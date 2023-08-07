# 3. **ist Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."

def func():
    arr=list(range(1,11))
    arr.append(8)
    arr.remove(5)
    arr.sort()
    print(arr)

if __name__ == "__main__":
    func()