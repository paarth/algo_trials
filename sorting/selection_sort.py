def swap_values(aList,i,j):
	temp = aList[i]
	aList[i] = aList[j]
	aList[j] = temp

def selection_sort(aList):
	for i in range(0,len(aList)-1):
		max_pos = 0
		for j in range(1,len(aList)-i):
			if aList[j]>aList[max_pos]:
				max_pos = j
		swap_values(aList,max_pos,len(aList)-1-i)


n = int(raw_input("Kindly enter the number of elements in your list: "))
print "Now kindly enter all the elemnts of your list, each element in searate line"
yourList = []
for i in range(0,n):
	yourList.append(int(raw_input()))

selection_sort(yourList)

print "Here is your sorted list\n", yourList