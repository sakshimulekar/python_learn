# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Flag to check if any swaps occur in this pass
        swapped = False

        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # If the element at j is greater than the element at j+1, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps occurred in this pass, the array is already sorted
        if not swapped:
            break

# Test the function
input_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(input_list)
print(input_list)
