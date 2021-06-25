t = int(input())            #enter the number of testcases
tsp1 = 0
tsp2 = 0
ans = [0,0]
for i in range(t):
    p1,p2 = map(int, input().split())       #two input values in single line
    tsp1 += p1
    tsp2 += p2

    #condition
    
    if tsp1 > tsp2:
        dif = tsp1 - tsp2       
        if dif > ans[1]:
            ans[0] = 1 
            ans[1] = dif
    else:
        dif = tsp2 - tsp1
        if dif>ans[1]:
            ans[0] = 2
            ans[1] = dif
print("{} {}".format(ans[0], ans[1]))       #inputs thevalues in the flower brackets
    
        
    
    
    
