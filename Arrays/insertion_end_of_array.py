# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        # used the length - 1 technique to target the final element of an array
        arr[length - 1] = n
        return arr

arr = [1,2,3,4,5]

print('without append ', insertEnd(arr, 6, 5, 10)) # [1,2,3,4,5,6]



# Alternate explanation for original code above

# The error message IndexError: list assignment index out of range in Python indicates that you're trying to access or modify an element in a list (arr in your case) at an index that doesn't exist.

# Here's what's happening in your code:

# The Situation: You're trying to insert a new element at the end of an array. In Python, arrays are actually lists, and they are zero-indexed. This means the first element is at index 0, the second at index 1, and so on.

# The Problem: When you try to insert a new element at the end of the list by accessing arr[length], you're actually going out of the current range of the list. For instance, if your list arr has 5 elements, its length is 5, but the valid indices are 0 to 4. So, trying to access arr[5] will give an IndexError.

# The Solution: To insert an element at the end of a list in Python, you should use the append() method instead of trying to assign a value to an out-of-range index. The append() method automatically adds the new element to the end of the list, handling the index issue internally.

# Here's how you can modify your function:

def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr.append(n)  # Use append() to add the element to the end

# Example array
# arr = [1, 2, 3, 4, 5]

# Call the function
insertEnd(arr, 6, len(arr), 10)

# Print the modified array
print('with append ', arr)  # Expected output: [1, 2, 3, 4, 5, 6]
