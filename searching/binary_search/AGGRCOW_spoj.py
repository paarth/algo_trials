def possible(curremt_distance,stall_location,c):
	n = len(stall_location)
	cnt = 1

	b = 0
	i = 1
	while i < n and cnt < c:
		if stall_location[i]-stall_location[b] >= curremt_distance:
			cnt += 1
			b = i
		i += 1
			
	if cnt >= c:
		return 1

	return 0

t = int(raw_input())

for test_case in range(0,t):
	n,c = map(int,raw_input().split())
	stall_location = []
	
	for i in range(0,n):
		stall_location.append(int(raw_input()))

	stall_location.sort()
	# print stall_location

	lo = 1
	hi = stall_location[n-1]-stall_location[0]+1

	while lo < hi:
		# print "hi,lo=",hi,lo
		mid = (lo+hi)//2
		if possible(mid,stall_location,c):
			lo=mid+1
		else:
			hi=mid

	print lo- int( not possible(lo,stall_location,c))

