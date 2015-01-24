def areAnagrams(s1,s2):
	if len(s1) != len(s2):
		return False

	list_of_str2 = list(s2)

	i=0
	false_detection_flag=False

	while i < len(s1) and false_detection_flag == False:
		j=0
		false_detection_flag = True

		while j < len(list_of_str2) and false_detection_flag == True:
			if s1[i] ==	list_of_str2[j]:
				false_detection_flag = False
				list_of_str2[j] = None
			else:
				j += 1
		i += 1

	return not false_detection_flag


inp_str1 = raw_input("Enter the first String: ")
inp_str2 = raw_input("Enter the second String: ")

print areAnagrams(inp_str1,inp_str2)
