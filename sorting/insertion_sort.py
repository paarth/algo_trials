def insertion_sort(aList):
	for i in range(1,len(aList)):
		cur_value = aList[i]
		cur_pos = i

		while cur_pos > 0 and aList[cur_pos-1] > cur_value:
			aList[cur_pos] = aList[cur_pos-1]
			cur_pos -= 1
			
		aList[cur_pos] = cur_value

n = int(raw_input("Kindly enter the number of elements in your list: "))
print "Now kindly enter all the elemnts of your list, each element in searate line"
yourList = []
for i in range(0,n):
	yourList.append(int(raw_input()))

insertion_sort(yourList)

print "Here is your sorted list\n", yourList