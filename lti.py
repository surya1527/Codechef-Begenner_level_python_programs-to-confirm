def nCr(n, r, m):

	return (fact(n) / (fact(r)
				* fact(n - r)))

# Returns factorial of n
def fact(n):

	res = 1
	
	for i in range(2, n+1):
		res = res * i

    
		
	return res%m

# Driver code
n = int(input())
r = int(input())
m = int(input())
print(int(nCr(n, r, m)))


