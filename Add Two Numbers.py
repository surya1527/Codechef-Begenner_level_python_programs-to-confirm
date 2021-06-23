T = int(input())   #Read the number of test cases.
for tc in range(T):

	(a, b) = map(int, input().split(' '))    	# Read integers a and b.
	
	ans = a + b
	print(ans)