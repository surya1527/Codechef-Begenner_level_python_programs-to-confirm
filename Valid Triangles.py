t=int(input())              #enter the number of test cases
for i in range (t):
    a , b , c = map(int,input().split())            #multiple input values
    
    #check the condition
 
    if (a+b+c == 180):
        print("YES")
    else:
        print("NO")