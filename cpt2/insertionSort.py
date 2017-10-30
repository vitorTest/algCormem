# insertion sort
# python's adaptation of Cormen's algorithm
def insertionSort(A):
	for j in range(1, len(A)):
		key = A[j]
		i 	= j - 1
		
		# Here, Cormen works with i > 0,
		# because he count from 1 until n-1.
		# In python's list we start
		# counting by 0, so we work with i > -1
		while i > -1 and A[i] > key:	
			A[i + 1] = A[i]				
			i = i - 1
		
		A[i + 1] = key

	print(A)

A = [3, 6, 2, 1, 7, 10, 5, 4, 8, 9]
insertionSort(A)