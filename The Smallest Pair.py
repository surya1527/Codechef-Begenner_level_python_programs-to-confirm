t= int(input())                     #enter the number of test cases
for i in range(t):
    
    N = int(input())
    aij = list(map(int,input().split()))               #takes the multiple inputs in the list
    aij.sort()                          #SORTS THE LIST
    c = (aij[:2])

    #logic to print the sum of 1st two elements in the list

    sum = 0 
    for i in range (0, len(c)):
        sum = sum + c[i]
    print(sum)