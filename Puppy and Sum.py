def calculate(D,N):             #define a function
    if D>1:                                 
        return calculate(D-1,N*(N+1)//2)        #sum of number till n is: n*(n+1)//2
    else:
        return N*(N+1)//2
for _ in range (int(input())):                  #Input the range of testcases
    A=list(map(int,input().split()))            #two inputs in a single line
    D,N = A[0],A[1]
    print(calculate(D,N))