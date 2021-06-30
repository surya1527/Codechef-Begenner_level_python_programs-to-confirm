t=int(input())                      #enter the number of testcases
for i in range(t):
    q , p = map(int,input().split())       #two input values in single line
    total=0
    #condition
    if q>1000:
        total = (q*p) *0.9                  
    else:
        total = (q*p)
    print('{0:.6f}'.format(total))          #six '0' after the outputvalue