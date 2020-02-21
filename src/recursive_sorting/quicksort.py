
my_list = [5, 9, 3, 7, 2, 8, 1, 6]

def partition(data):
	pivot = data[0]
	left = []
	right = []

	for item in data[1:]:
		if item < pivot:
			left.append(item)
		else:
			right.append(item)

	return pivot, left, right

def quicksort(data):
	if data == []:
		return data

	pivot, left, right = partition(data)

	return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(my_list))