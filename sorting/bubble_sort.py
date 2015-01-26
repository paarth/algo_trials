def bubble_sort(aList):
	swaps = True
	for pass_number in range(len(aList)-1,0,-1):
		swaps = False
		for i in range(0,pass_number):
			if aList[i]>aList[i+1]:
				swaps = True
				temp = aList[i]
				aList[i] = aList[i+1]
				aList[i+1] = temp
		if swaps == False:
			break

n = int(raw_input("Kindly enter the number of elements in your list: "))
print "Now kindly enter all the elemnts of your list, each element in searate line"
yourList = []
for i in range(0,n):
	yourList.append(int(raw_input()))

bubble_sort(yourList)

print "Here is your soorted list\n", yourList