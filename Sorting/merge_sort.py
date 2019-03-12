#-----------------------------------
#|---------------------------------|
#|        Merge Sort:              |
#|---------------------------------|
#-----------------------------------
# Description: 
#   It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. 

# Python code:

#-----------------------------------#-----------------------------------
def merge_sort(arr): 
    if len(arr) <= 1:
        return arr
    
    mid = int(len(arr)/2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge 2 sorted arrays
    result = []
    i = 0  # index for left
    j = 0  # index for right
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # either one of the array is empty
    result += left[i:]
    result += right[j:]
    return result
#-----------------------------------#-----------------------------------

# Time Complexity: O(nLgn)

# Auxiliary Space: O(n)

# In Place : No

# Stable: Yes
