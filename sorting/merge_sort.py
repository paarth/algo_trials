def merge_sort(aList):

	# Splitting Or divide Step
	if len(aList) > 1:
		mid = len(aList)//2
		left_half = aList[:mid]
		right_half = aList[mid:]

		merge_sort(left_half)
		merge_sort(right_half)

		# Merging Or conquer step
		ptr_i = 0
		ptr_j = 0
		ptr_k = 0

		while ptr_i < len(left_half) and ptr_j < len(right_half):
			if left_half[ptr_i] < right_half[ptr_j]:
				aList[ptr_k] = left_half[ptr_i]
				ptr_i += 1
				ptr_k += 1
			else:
				aList[ptr_k] = right_half[ptr_j]
				ptr_j += 1
				ptr_k += 1

		while ptr_i < len(left_half):
			aList[ptr_k] = left_half[ptr_i]
			ptr_i += 1
			ptr_k += 1

		while ptr_j < len(right_half):
			aList[ptr_k] = right_half[ptr_j]
			ptr_j += 1
			ptr_k += 1

n = int(raw_input("Kindly enter the number of elements in your list: "))
print "Now kindly enter all the elemnts of your list, each element in searate line"
yourList = []
for i in range(0,n):
	yourList.append(int(raw_input()))

merge_sort(yourList)

print "Here is your sorted list\n", yourList