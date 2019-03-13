def seq_search(arr, elem):
	"""
	returns the index where elem is found, otherwise return -1
	"""
	pos = 0
	found = False

	while pos < len(arr) and not found:
		if arr[pos] == elem:
			found = True
			return pos
		else:
			pos += 1

	return -1

def ordered_seq_search(arr, elem):
	"""
	the function takes an sorted/ordered array
	returns the index where elem is found, otherwise return -1
	"""
	pos = 0
	found = False
	stopped = False 	#stopped when the item in the array > elem

	while pos < len(arr) and not found and not stopped:
		if arr[pos] == elem:
			found = True
			return pos
		else:
			if arr[pos] > elem:
				stopped = True
			else:
				pos += 1

	return -1

