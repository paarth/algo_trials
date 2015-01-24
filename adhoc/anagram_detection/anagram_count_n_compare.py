def areAnagrams(s1,s2):
	if len(s1) != len(s2):
		return False

	count_of_str1 = [0]*26
	count_of_str2 = [0]*26	
	
	# populating count for string1 and string2 together
	for i in range(0,len(s1)):
		count_of_str1[ord(s1[i])-ord('a')] += 1
		count_of_str2[ord(s2[i])-ord('a')] += 1

	false_detection_flag=False
	# now iterating through the count lists and comparing

	for i in range(0,len(count_of_str1)):
		if count_of_str1[i] != count_of_str2[i]:
			false_detection_flag = True
			break

	return not false_detection_flag


inp_str1 = raw_input("Enter the first String: ")
inp_str2 = raw_input("Enter the second String: ")

print areAnagrams(inp_str1,inp_str2)
