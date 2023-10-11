# Python3 program for the above approach

# Function to implement bubble
# sort without using loops
def bubble_sort(ar):

	# Base Case: If array
	# contains a single element
	if len(ar) <= 1:
		return ar
	
	# Base Case: If array
	# contains two elements
	if len(ar) == 2:
		return ar if ar[0] < ar[1] else [ar[1], ar[0]]

	# Store the first two elements
	# of the list in variables a and b
	a, b = ar[0], ar[1]

	# Store remaining elements
	# in the list bs
	bs = ar[2:]

	# Store the list after
	# each recursive call 
	res = []
	
	# If a < b 
	if a < b:
		res = [a] + bubble_sort([b] + bs)
		
	# Otherwise, if b >= a
	else:
		res = [b] + bubble_sort([a] + bs)
		
	# Recursively call for the list
	# less than the last element and
	# and return the newly formed list
	return bubble_sort(res[:-1]) + res[-1:]


# Driver Code

arr = [1, 3, 4, 5, 6, 2]
res = bubble_sort(arr)

# Print the array
print(*res)
