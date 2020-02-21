# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        temp_value = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp_value

    return arr


newarray = [9, 6, 1, 3, 2, 7, 4, 5, 8]
print(selection_sort(newarray))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # swap = True
    # Loop through your array
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        # - Compare each element to its neighbor
        # - If elements in wrong position (relative to each other, swap them)
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    return arr


newarray = [9, 6, 1, 3, 2, 7, 4, 5, 8]
print(bubble_sort(newarray))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
	count = [0] * maximum
	sorted_arr = []
	for item in range(0, len(arr) - 1):
		count.append(0)
		if arr[item] < 0:
			return "Error, negative numbers not allowed in Count Sort"
		elif arr[item] >= 0:
			count[arr[item]] += 1
			item += 1
	for j in range(0, len(count)):
		while count[j] > 0:
			sorted_arr.append(j)
			count[j] -= 1
	return sorted_arr

newarray = [9, 6, 8, 3, 2, -7, 2, 5, 8]
print(count_sort(newarray, 10))
