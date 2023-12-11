# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted
        print(arr)
    
arr = [1, 2, 3, 4, 5]

print(removeMiddle(arr, 5, 5))

# In the worst case, n - 1 shifts may be required. Therefore, the code above is O(n).

#  Below are the outputs when I change the value of the second parameter 'i' in the removeMiddle function
# The function iterates starting on the 'i' value which is then used to remove the value at index 'i' then it will shift the elements to the left

# 0 index
# [2, 2, 3, 4, 5]
# [2, 3, 3, 4, 5]
# [2, 3, 4, 4, 5]
# [2, 3, 4, 5, 5]
# None

# 1 Index
# [1, 3, 3, 4, 5]
# [1, 3, 4, 4, 5]
# [1, 3, 4, 5, 5]
# None

# 2 Index
# [1, 2, 4, 4, 5]
# [1, 2, 4, 5, 5]
# None

# 3 index
# [1, 2, 3, 5, 5]
# None

# 4 index 
# None

# 5 index
# None