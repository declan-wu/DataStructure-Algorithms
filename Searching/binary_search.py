
def binary_search(arr, elem):
	"""
	iterative method
	this function takes an sorted array
	-1 return value indicates not found
	"""
	first = 0 
	last = len(arr) - 1

	while first <= last:
		mid = (first + last) // 2
		if arr[mid] == elem:
			return mid
		elif arr[mid] > elem:
			last = mid - 1
		else:
			first = mid + 1

	return -1


def recur_bin_search(arr, elem):
	"""
	recursive method
	this function takes an sorted array
	-1 return value indicates not found
	"""
	first = 0 
	last = len(arr) - 1
	return recur_helper(arr, elem, first, last)

def recur_helper(arr, elem, first, last):
	if first <= last:
		mid = (first + last) // 2
		if arr[mid] == elem:
			return mid
		elif arr[mid] > elem:
			last = mid - 1
			return recur_helper(arr, elem, first, last)
		else:
			first = mid + 1
			return recur_helper(arr, elem, first, last)
	return -1

def rec_bin_search(arr,elem):
	"""
	recursive method without using a helper function, but use array index slicing
	"""
    # Base Case
    if len(arr) == 0:
        return False
    
    # Recursive Case
    else:     
        mid = len(arr)/2   
   
        if arr[mid]==elem:
            return True
        else:          
            if ele<arr[mid]:
                return rec_bin_search(arr[:mid],elem)   
            else:
                return rec_bin_search(arr[mid+1:],elem)


