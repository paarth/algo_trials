def areAnagrams(s1,s2):
	if len(s1) != len(s2):
		return False

	list_of_str1 = list(s1)
	list_of_str2 = list(s2)

	list_of_str1.sort()
	list_of_str2.sort()

	false_detection_flag=False

	for i in range(0,len(list_of_str1)):
		if list_of_str1[i] != list_of_str2[i]:
			false_detection_flag = True
			break

	return not false_detection_flag


inp_str1 = raw_input("Enter the first String: ")
inp_str2 = raw_input("Enter the second String: ")

print areAnagrams(inp_str1,inp_str2)
