# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
	elements = len(arrA) + len(arrB)
	merged_arr = [0] * elements

	# Set counter variables
	a = 0
	b = 0

	# Loop through the indeces in the merged array
	for i in range(len(merged_arr)):
		# First array has no more items to check
		if a == len(arrA):
			merged_arr[i] = arrB[b]
			b += 1

		# Second array has no more items to check
		elif b == len(arrB):
			merged_arr[i] = arrA[a]
			a += 1
		
		# One is larger than the other
		elif arrA[a] <= arrB[b]:
			merged_arr[i] = arrA[a]
			a += 1
		elif arrA[a] >= arrB[b]:
			merged_arr[i] = arrB[b]
			b += 1
	return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
	# Array is too short to split: base case
	if len(arr) <= 1:
		return arr
	# Until base case, recurse:
	else:
		half = len(arr) // 2
		left = merge_sort(arr[:half])
		right = merge_sort(arr[half:])
		arr = merge(left, right)
	return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):

	return arr


def merge_sort_in_place(arr, l, r):
# TO-DO

	return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

	return arr
