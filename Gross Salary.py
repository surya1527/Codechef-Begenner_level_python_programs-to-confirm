t = int(input())        #enter the number of testcases
for i in range(t):          
    s = int(input())        #input the salary

    #initializations

    hra = 0
    da = 0
    gs = 0

    #conditions
    
    if (s<1500):
        hra = 0.1 * s
        da = s-hra
    elif (s >= 1500):
        hra = 500
        da = s * 0.98

    gs = s + da + hra
    print(gs)


