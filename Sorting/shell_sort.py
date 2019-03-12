#-----------------------------------
#|---------------------------------|
#|        Shell Sort:              |
#|---------------------------------|
#-----------------------------------
# Description: 
#   Choose a gap, usually N/2, and then starting from the index 0, group the elements by every gap,
#   Let say gap is 4, then index 0, 4, 8. Fisrt key is 4, insersion sort on 0, 4, then, increment key.
#   insersion sort on index 1, 5. then increment key until the last element. The final pass would be 
#   like an insersion sort. 

# Python code:
#-----------------------------------#-----------------------------------    
def shell_sort(arr): 
    gap = len(arr) // 2 
    while gap > 0:
        gap_insertion_sort(arr, gap)
        gap = gap // 2

def gap_insertion_sort(lst, gap):
    for pass_numer in range(gap):
        arr = lst[pass_numer:]
        for i in range(0+gap,len(arr),gap):
            key = arr[i]
            j = i - gap     # j is the last index of sorted array
            while j >= 0 and arr[j] > key:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = key
        lst[pass_numer:] = arr
#-----------------------------------#-----------------------------------
        
# Demo.
#   0. Gap = int(N/2) = 2
#   0. arr[] = 64 25 12 22 11
#   1. arr[] = 11 25 12 22 64 --insersion sort on 64, 12, 11
#   2. arr[] = 11 22 12 25 64 --insersion sort on 25, 22
#   3. Gap = Gap/2 = 1
#   3. arr[] = 11 12 22 25 64 --insersion sort on all elements

# Time Complexity: O(n^2) ?????? idk...

# Auxiliary Space: O(1)

# In Place : No

# Stable: No

