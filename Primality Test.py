t= int(input())                     #enter the number of testcases
for i in range (t):

    num = int(input())              #enter the number
    
  
    if num > 1:             #if the number is greater than 1
    
    	# Iterate from 2 to n / 2
    	for i in range(2, int(num/2)+1):            #if remiander is zere when it is divided by other than zero then it is prime
    
    		if (num % i) == 0:
    			print("no")
    			break                        #exit from the loop to avoid external conditions
    	else:
    		print("yes")
    
    else:
    	print("no")
