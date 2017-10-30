# first and quick algorithm to sort
# before read Cormen's algorithms
# vflix
def sort(aList):
	for index in range(1, len(aList)):
		key = aList[index]
		pre	= aList[index - 1]
		j 	= index

		while key < pre and j > 0: 
			aList[j - 1] = key
			aList[j]	 = pre

			j = j - 1

			key = aList[j]
			pre = aList[j-1]

	print(aList)

aList = [3, 6, 2, 1, 7, 10, 5, 4, 8, 9]
sort(aList)