t = int(input())            #input the number of test cases
def factorial(n):            # Function to find factorial of given number
	
	if n == 0:
		return 1
	
	return n * factorial(n-1)       

# Driver Code
for i in range(t):
    num = int(input())          #enter the input
    print(factorial(num))
