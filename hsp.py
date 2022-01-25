n = int(input())
def averageValue(s):
	sum_char = 0

	for i in range(len(s)):
		sum_char += ord(s[i])


	return sum_char // len(s)




# Driver code
if __name__ == "__main__":
	
	s = "asp"

	print(averageValue(s))

