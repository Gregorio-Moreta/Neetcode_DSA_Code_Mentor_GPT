def removeMiddle(arr, i, length):
    # Shift elements starting from index i + 1 to the left.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
        
    # Remove the last element as it's now duplicated.
    arr.pop()

# Example array
arr = [4, 5, 6]

# Length of the array
length = len(arr)

# Call the function to remove the element at index 1 (which is 5)
removeMiddle(arr, 1, length)

# Print the modified array
print(arr)  # Output will be [4, 6]

