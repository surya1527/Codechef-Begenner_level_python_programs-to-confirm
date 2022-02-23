def notPresent(c,arr):

	for i in range(len(arr)):
		j = 0
		while(j < len(arr)):
			if (i != j and arr[i] == arr[j]):
				break
			j += 1
		if (j == len(arr)):
			return arr[i]
            
	return -1
	
# Driver code
c = int(input())
arr=list(map(int,input().split()))
print(notPresent(c,arr))
