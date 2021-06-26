t= int(input())                 #enter the number of testcases
for i in range (t):
    fact = 1                    #initialize
    n = int(input())                #input the number
    while(n>0):
        fact = n * fact
        n-=1
    print(fact)
