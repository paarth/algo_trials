def swap_values(aList,i,j):
	temp = aList[i]
	aList[i] = aList[j]
	aList[j] = temp

def partition(aList,start,end):
	pivot = aList[start]

	left_ptr = start + 1
	right_ptr = end

	while left_ptr <= right_ptr:

		while left_ptr <= right_ptr and aList[left_ptr] <= pivot:
			left_ptr += 1
		while left_ptr <= right_ptr and aList[right_ptr] >= pivot:
			right_ptr -= 1
		if right_ptr < left_ptr:
			break
		else:
			swap_values(aList,left_ptr,right_ptr)

	swap_values(aList,start,right_ptr)

	return right_ptr

def quick_sort_helper(aList,start,end):
	
	if start < end:
		split_pos = partition(aList,start,end)
	
		quick_sort_helper(aList,start,split_pos-1)
		quick_sort_helper(aList,split_pos+1,end)

def quick_sort(aList):
	quick_sort_helper(aList,0,len(aList)-1)


n = int(raw_input("Kindly enter the number of elements in your list: "))
print "Now kindly enter all the elemnts of your list, each element in searate line"
yourList = []
for i in range(0,n):
	yourList.append(int(raw_input()))

quick_sort(yourList)

print "Here is your sorted list\n", yourList