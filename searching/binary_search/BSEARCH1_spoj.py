from bisect import bisect_left

n,q = map(int,raw_input().split())
A = map(int,raw_input().split())

for test_case in range(0,q):
	val = int(raw_input())
	pos = bisect_left(A,val)	
	if pos >= 0 and pos < len(A) and A[pos] == val:
		print pos
	else:
		print "-1"






